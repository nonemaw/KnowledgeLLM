import os
import pickle
import shutil
from datetime import datetime
from functools import wraps
from threading import Event, Lock
from typing import Any, Callable

from constants.lib_constants import (LIB_DATA_FOLDER, SORTED_BY_LABELS,
                                     SUPPORTED_EXTENSIONS, VIEW_STYLES)
from library.embedding_record_table import EmbeddingRecordTable
from library.lib_item import *
from loggers import lib_logger as LOGGER
from utils.errors.lib_errors import LibraryError
from utils.file_operator import FileOperator

DEFAULT_EXCLUSION_LIST: set[str] = {
    '$RECYCLE.BIN',
    'System Volume Information',
    'Thumbs.db',
    'desktop.ini',
    '.DS_Store',
    '.localized',
    '__pycache__',
    'node_modules',
    LIB_DATA_FOLDER,  # The folder for library's data
}

BASIC_METADATA: dict = {
    'type': '',
    'uuid': '',  # UUID of the library
    'name': '',
    'created_on': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'view_style': 'grid',
    'sorted_by': 'name',
    'favorite_list': set(),
    'exclusion_list': DEFAULT_EXCLUSION_LIST,
}


def ensure_lib_is_ready(func):
    """Decorator to ensure the library is ready before calling the function
    """
    @wraps(func)
    def wrapper(self: 'LibraryBase', *args, **kwargs):
        if not self.is_ready():
            raise LibraryError(f'Library is not ready: {self.path_lib}')
        return func(self, *args, **kwargs)
    return wrapper


def ensure_metadata_ready(func):
    """Decorator to ensure the library's metadata exists
    """
    @wraps(func)
    def wrapper(self: 'LibraryBase', *args, **kwargs):
        if not self._metadata:
            raise LibraryError(f'Library is not ready, metadata not initialized: {self.path_lib}')
        return func(self, *args, **kwargs)
    return wrapper


class LibraryBase:

    # Metadata for the library
    METADATA_FILE: str = 'metadata.bin'

    def __init__(self, lib_path: str):
        LOGGER.info(f'Instanizing library: {lib_path}')

        # Expand the lib path to absolute path
        lib_path = os.path.expanduser(lib_path)
        if not os.path.isdir(lib_path):
            raise LibraryError(f'Invalid lib path: {lib_path}')

        # UUID of the library
        self.uuid: str = ''
        # The current relative path user is browsing under the library
        self.current_path: str = ''

        # Static path info - these paths are not supposed to be changed after library's initialization
        # Path to the library root folder
        self.path_lib: str = lib_path
        # Path to the library's data folder
        self._path_lib_data: str = os.path.join(self.path_lib, LIB_DATA_FOLDER)
        # Path to the library metadata file
        self.__path_metadata: str = os.path.join(self._path_lib_data, LibraryBase.METADATA_FILE)

        # In-memory library metadata
        self._metadata: dict = dict()
        # Table that tracks the embedding status of files under the library
        self._embedding_table: EmbeddingRecordTable | None = None

        # File scan is mutually exclusive, use a lock to prevent concurrent operations such as scan and file moving
        self._file_lock: Lock = Lock()
        # File operator
        self._file_operator: FileOperator = FileOperator(root_path=self.path_lib)

        # Ensure the library's data folder exists
        if not os.path.isdir(self._path_lib_data):
            os.makedirs(self._path_lib_data)

    """
    Library methods for override
    """

    def set_embedder(self, embedder: Any):
        """Set embedder for library

        Embedder initialization is apart from initialize(), it is easy to switch to another embedder without a re-initialization
        """
        raise NotImplementedError()

    def is_ready(self) -> bool:
        """Check if the library is ready for use
        - If not, means only the metadata file created
        """
        raise NotImplementedError()

    def demolish(self):
        """Completely destroy the library
        """
        raise NotImplementedError()

    def full_scan(self,
                  force_init: bool = False,
                  progress_reporter: Callable[[int, int, str | None], None] | None = None,
                  cancel_event: Event | None = None):
        """Initialize the library

        Args:
            force_init (bool, optional): If the initialization is a force re-initialization. Defaults to False.
            reporter (Callable[[int, int, str | None], None] | None, optional): The reporter function which reports progress to task runner
            It accepts a integer from 0~100 to represent current progress of initialization. Defaults to None.
            cancel_event (Event | None, optional): The event object to check if the initialization is cancelled. Defaults to None.
        """
        raise NotImplementedError()

    def use_doc(self,
                relative_path: str,
                provider_type: Any,
                force_init: bool = False,
                progress_reporter: Callable[[int, int, str | None], None] | None = None,
                cancel_event: Event | None = None):
        """Initialize or switch to a document under current library
        - If target document is not in metadata, then this is an uninitialized document, call __initialize_doc()
        - Otherwise load the document provider and vector DB for the target document directly
        - Target document's provider type is mandatory

        Args:
            relative_path (str): The target document's relative path based on current library
            provider_type (Type[D]): The target document's provider's type info
            force_init (bool, optional): If the initialization is a force re-initialization, this will delete doc's previous embeddings (if any). Defaults to False.
            reporter (Callable[[int, int, str | None], None] | None, optional): The reporter function which reports progress to task runner
            It accepts a integer from 0~100 to represent current progress of initialization. Defaults to None.
            cancel_event (Event | None, optional): The event object to check if the initialization is cancelled. Defaults to None.
        """
        raise NotImplementedError()

    def delete_file_embedding(self, relative_path: str) -> bool:
        """Delete the embedding of given file but keep the file on disk
        """
        raise NotImplementedError()

    """
    File/folder A/R/W/D operation methods
    - Do pre-checks and call the file operator to do the actual work
    """

    def add_files(self, target_relative_path: str, source_file: str) -> bool:
        raise NotImplementedError()

    def move_files(self, relative_paths: list[str], dest_folder_relative_path: str) -> bool:
        """Move a list of files/folders under current library to a target folder, and retain the existing embedding information

        Args:
            relative_paths (list[str]): A list of relative paths of the files/folders to be moved
            dest_folder_relative_path (str): Relative path of the target folder to move the files/folders to
        """
        if not relative_paths or dest_folder_relative_path is None:
            return False

        all_success: bool = True
        dest_folder_relative_path = dest_folder_relative_path.strip().lstrip(os.path.sep)
        for relative_path in relative_paths:
            relative_path = relative_path.strip().lstrip(os.path.sep)
            LOGGER.info(f'Prepare to move item from {relative_path} to {dest_folder_relative_path}')
            full_path: str = os.path.join(self.path_lib, relative_path)
            if not os.path.exists(full_path):
                continue

            name: str = os.path.basename(relative_path)
            new_relative_path: str = os.path.join(dest_folder_relative_path, name)
            if relative_path == new_relative_path:
                continue

            # Update the scan record with new relative path to retain the embedding information
            if os.path.isfile(full_path):
                all_success = self._file_operator.move_file(relative_path,
                                                            new_relative_path,
                                                            is_rename=False,
                                                            update_record=self._embedding_table.update_record_by_relative_path) and all_success  # type: ignore
            else:
                all_success = self._file_operator.move_folder(relative_path,
                                                              new_relative_path,
                                                              is_rename=False,
                                                              update_record=self._embedding_table.update_record_by_relative_path) and all_success  # type: ignore
        return all_success

    def rename_file(self, relative_path: str, new_name: str) -> bool:
        """Rename the given file/folder under current library and retain the existing embedding information

        Args:
            relative_path (str): The relative path of the target file/folder to be renamed
            new_name (str): The new file/folder name
        """
        if not relative_path or not new_name:
            return False
        relative_path = relative_path.strip().lstrip(os.path.sep)
        new_name = new_name.strip()
        if not relative_path or not new_name:
            return False

        # Simple invalid new name cases
        if new_name.startswith(os.path.sep) or new_name in ('.', '..'):
            LOGGER.warning(f'Invalid new name: {new_name}, skip renaming')
            return False

        LOGGER.info(f'Prepare to rename item {relative_path} with new name: {new_name}')
        full_path: str = os.path.join(self.path_lib, relative_path)
        if not os.path.exists(full_path):
            return False

        name: str = os.path.basename(relative_path)
        if name == new_name:
            return True

        # Update the scan record with new relative path to retain the embedding information
        new_relative_path = os.path.join(os.path.dirname(relative_path), new_name)
        if os.path.isfile(full_path):
            return self._file_operator.move_file(relative_path,
                                                 new_relative_path,
                                                 is_rename=True,
                                                 update_record=self._embedding_table.update_record_by_relative_path)  # type: ignore
        else:
            return self._file_operator.move_folder(relative_path,
                                                   new_relative_path,
                                                   is_rename=True,
                                                   update_record=self._embedding_table.update_record_by_relative_path)  # type: ignore

    def delete_files(self, relative_paths: list[str]) -> bool:
        """Delete the given files/folders from disk and its embedding

        Args:
            relative_paths (list[str]): A list of relative paths of the files/folders to be deleted
        """
        if not relative_paths:
            return False

        all_success: bool = True
        for relative_path in relative_paths:
            LOGGER.info(f'Prepare to delete item: {relative_path}')
            relative_path = relative_path.strip().lstrip(os.path.sep)
            if not relative_path:
                continue

            full_path: str = os.path.join(self.path_lib, relative_path)
            if not os.path.exists(full_path):
                continue

            # Delete embedding first, if success then delete the file
            if os.path.isfile(full_path):
                LOGGER.info(f'Delete file {relative_path} from library')
                if self.delete_file_embedding(relative_path):
                    all_success = self._file_operator.delete_file(relative_path) and all_success
                else:
                    all_success = False
            else:
                folder_success: bool = True
                LOGGER.info(f'Delete folder {relative_path} from library')
                for r in self._file_operator.folder_walker(relative_path):
                    if self.delete_file_embedding(r):
                        folder_success = self._file_operator.delete_file(r) and folder_success
                    else:
                        folder_success = False

                all_success = folder_success and all_success
                if folder_success:
                    shutil.rmtree(full_path)
                    LOGGER.info(f'Folder {relative_path} deleted')
                else:
                    LOGGER.info(f'Not all files under folder {relative_path} are successfully deleted')

        return all_success

    def list_folder_content(self, folder_relative_path: str) -> tuple[list[DirectoryItem], list[FileItem]]:
        """List the content of a folder, no recursion

        Args:
            folder_relative_path (str): The relative path of the folder to be scanned, starting from the root of current library
        """
        dir_list: list[DirectoryItem] = list()
        file_list: list[FileItem] = list()

        # Empty string is acceptable (listing the root of the library) but None is not
        if folder_relative_path is None:
            return dir_list, file_list

        folder_relative_path = folder_relative_path.strip().lstrip(os.path.sep)
        folder_full_path: str = os.path.join(self.path_lib, folder_relative_path)
        if not os.path.isdir(folder_full_path):
            return dir_list, file_list

        LOGGER.info(f'Listing folder content: {folder_relative_path}')
        for item_name in os.listdir(folder_full_path):
            item_path: str = os.path.join(folder_full_path, item_name)

            if os.path.isdir(item_path):
                dir_relative_path: str = os.path.join(folder_relative_path, item_name)
                if not self.is_accessible(dir_relative_path):
                    continue

                d_item: DirectoryItem = DirectoryItem()
                d_item.name = item_name
                d_item.parent_path = folder_relative_path
                try:
                    d_stats: os.stat_result = os.stat(item_path)
                    d_item.dtc = datetime.utcfromtimestamp(d_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                    d_item.dtm = datetime.utcfromtimestamp(d_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                except BaseException:
                    d_item.dtc = '-'
                    d_item.dtm = '-'
                dir_list.append(d_item)

            else:
                file_relative_path: str = os.path.join(folder_relative_path, item_name)
                if not self.is_accessible(file_relative_path):
                    continue

                f_item: FileItem = FileItem()
                f_item.name = item_name
                f_item.parent_path = folder_relative_path

                _, extension = os.path.splitext(item_name)
                if extension:
                    extension[1:].lower()
                f_item.extension = extension
                f_item.supported = extension in SUPPORTED_EXTENSIONS
                f_item.embedded = self._embedding_table.relative_path_exists(file_relative_path)  # type: ignore
                try:
                    f_stats: os.stat_result = os.stat(item_path)
                    f_item.dtc = datetime.utcfromtimestamp(f_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                    f_item.dtm = datetime.utcfromtimestamp(f_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    f_item.size_b = f_stats.st_size
                except BaseException:
                    f_item.dtc = '-'
                    f_item.dtm = '-'
                    f_item.size_b = -1
                file_list.append(f_item)

        LOGGER.info(f'Folder content listed, found: {len(dir_list)} folders, {len(file_list)} files')
        return dir_list, file_list

    def is_accessible(self, relative_path: str) -> bool:
        """Check if the given relative path is accessible under the library
        - Accessible means the file or folder is not in the exclusion list and it is under currently active library
        """
        if not relative_path:
            return True
        relative_path = relative_path.strip().lstrip(os.path.sep)
        if not relative_path:
            return True

        exclusion_list: set[str] = self.get_exclusion_list()
        if exclusion_list:
            file_or_folder_name: str = os.path.basename(relative_path)
            if file_or_folder_name in exclusion_list or relative_path in exclusion_list:
                return False
        full_path: str = os.path.join(self.path_lib, relative_path)
        return os.path.exists(full_path)

    """
    Embedding methods
    """

    def is_embedded(self, relative_path: str) -> bool:
        """Check if the given file is embedded
        """
        if not relative_path:
            return False
        relative_path = relative_path.strip().lstrip(os.path.sep)
        full_path: str = os.path.join(self.path_lib, relative_path)
        if not os.path.isfile(full_path):
            return False

        return self._embedding_table.relative_path_exists(relative_path)  # type: ignore

    def get_embedded_files(self) -> dict[str, str]:
        """Get the embedded files under the library with [relative_path: UUID]
        """
        res: list[tuple] = self._embedding_table.get_all_records()  # type: ignore

        # Row format: (id, timestamp, ongoing, uuid, relative_path)
        return {r[4]: r[3] for r in res}

    """
    Metadata file methods
    """

    def _save_metadata(self):
        """Save the metadata file for any updates
        """
        if not os.path.isfile(self.__path_metadata):
            raise LibraryError(f'Metadata file missing: {self.__path_metadata}')

        LOGGER.info('Saving metadata')
        pickle.dump(self._metadata, open(self.__path_metadata, 'wb'))

    def _metadata_exists(self) -> bool:
        """Check if the metadata exists
        """
        return os.path.isfile(self.__path_metadata)

    def initialize_metadata(self, initial: dict):
        """Initialize the metadata for the library
        - Only called when the library is under a fresh initialization (metadata file not exists), the UUID should not be changed after this
        - File missing or modify the UUID manually will cause the library's index missing
        """
        if not initial or not initial.get('uuid'):
            raise LibraryError('Invalid initial data')

        LOGGER.info('Initializing metadata')
        self._metadata = initial
        self.uuid = initial['uuid']
        pickle.dump(initial, open(self.__path_metadata, 'wb'))

    def load_metadata(self, given_uuid: str, given_name: str):
        """Load the metadata of the library
        """
        LOGGER.info('Loading metadata')
        try:
            content: dict = pickle.load(open(self.__path_metadata, 'rb'))
        except BaseException:
            raise LibraryError(f'Invalid metadata file: {self.__path_metadata}')
        if not content:
            raise LibraryError(f'Invalid metadata file: {self.__path_metadata}')
        if not content.get('uuid', None) or content['uuid'] != given_uuid:
            raise LibraryError(f'Metadata UUID mismatched: {self.__path_metadata}')

        self._metadata = content
        self.uuid = content['uuid']
        if content['name'] != given_name:
            self.change_lib_name(given_name)

    def delete_metadata(self):
        """Delete the metadata file of the library
        - Can only call on the deletion of current library
        """
        LOGGER.info('Deleting metadata')
        if os.path.isfile(self.__path_metadata):
            os.remove(self.__path_metadata)

    """
    Public methods to read library metadata
    """

    @ensure_metadata_ready
    def get_lib_name(self) -> str:
        return self._metadata['name']

    @ensure_metadata_ready
    def get_view_style(self) -> str:
        return self._metadata['view_style']

    @ensure_metadata_ready
    def get_sorted_by(self) -> str:
        return self._metadata['sorted_by']

    @ensure_metadata_ready
    def get_favorite_list(self) -> set[str]:
        return self._metadata['favorite_list']

    @ensure_metadata_ready
    def get_exclusion_list(self) -> set[str]:
        return self._metadata['exclusion_list']

    """
    Public methods to change library metadata
    """

    @ensure_metadata_ready
    def change_lib_name(self, new_name: str):
        if not new_name or new_name == self._metadata['name']:
            return

        LOGGER.info(f'Changing library name: {self._metadata["name"]} -> {new_name}')
        self._metadata['name'] = new_name
        self._save_metadata()

    @ensure_metadata_ready
    def change_view_style(self, new_style: str):
        if not new_style or new_style not in VIEW_STYLES:
            return

        LOGGER.info(f'Changing view style: {self._metadata["view_style"]} -> {new_style}')
        self._metadata['view_style'] = new_style
        self._save_metadata()

    @ensure_metadata_ready
    def change_sorted_by(self, new_sorted_by: str):
        if not new_sorted_by or new_sorted_by not in SORTED_BY_LABELS:
            return

        LOGGER.info(f'Changing sorted by: {self._metadata["sorted_by"]} -> {new_sorted_by}')
        self._metadata['sorted_by'] = new_sorted_by
        self._save_metadata()
