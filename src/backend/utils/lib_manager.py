import os
import pickle

from constants.env import CONFIG_FOLDER
from constants.lib_constants import LibTypes
from knowledge_base.document.doc_embedder import DocEmbedder
from knowledge_base.image.image_embedder import ImageEmbedder
from library.document.doc_lib import DocumentLib
from library.image.image_lib import ImageLib
from library.lib_base import LibraryBase
from loggers import lib_manager_logger as LOGGER
from utils.errors.lib_errors import LibraryError, LibraryManagerException
from utils.task_runner import TaskRunner

UUID_EMPTY: str = '00000000-0000-0000-0000-000000000000'
CONFIG_FILE: str = 'librarian.cfg'


class LibInfo:
    """Define a library object for server side to create and use
    """

    def __init__(self):
        self.name: str = ''  # The only modifiable field
        self.uuid: str = ''
        self.path: str = ''
        self.type: str = ''

    def to_dict(self) -> dict[str, str]:
        return {
            'name': self.name,
            'uuid': self.uuid,
            'path': self.path,
            'type': self.type
        }


class LibraryManager:
    """This is a single threaded, single session app, so one manager instance globally is enough
    """

    def __init__(self, task_runner: TaskRunner):
        if not task_runner:
            raise LibraryManagerException('Task runner is not provided')

        self.task_runner: TaskRunner = task_runner
        self.__path_config: str = os.path.join(CONFIG_FOLDER, CONFIG_FILE)
        # KV: uuid -> Library
        self.__libraries: dict[str, LibInfo] = dict()
        # Current library instance
        self.instance: LibraryBase | None = None

        LOGGER.info('Loading config file')
        current_lib: str = ''
        try:
            if not os.path.isfile(self.__path_config):
                obj: dict = dict()
            else:
                obj: dict = pickle.load(open(self.__path_config, 'rb'))
                self.__libraries = obj['libraries']
                current_lib = obj['current_lib']

            LOGGER.info(f'Found {len(self.__libraries)} libraries in config file')
            if current_lib:
                LOGGER.info(f'Found active library: {current_lib}, try to instanize it')
                if current_lib not in self.__libraries:
                    LOGGER.warn('Active library is not in library list, config file might be corrupted, active library ignored')
                else:
                    self.__instanize_lib(current_lib)
        except BaseException:
            raise LibraryManagerException('Config file corrupted')

    def __save(self):
        pickle.dump(
            {
                'libraries': self.__libraries,
                'current_lib': self.instance.uuid if self.instance else ''
            },
            open(self.__path_config, 'wb'))

    """
    Get current library information
    """

    def get_current_lib_info(self) -> LibInfo | None:
        """Get the general info of current library
        """
        if not self.instance:
            return None
        return self.__libraries[self.instance.uuid]

    def lib_exists(self, uuid: str) -> bool:
        return uuid in self.__libraries

    def get_library_list(self) -> list[LibInfo]:
        """Get the list of all existing libraries, sorted
        """
        res: list[LibInfo] = [self.__libraries[uuid] for uuid in self.__libraries]
        res.sort(key=lambda x: x.name)
        return res

    def get_library_path_list(self) -> list[str]:
        """Get the list of all libraries (lib paths), sorted
        """
        res: list[str] = [self.__libraries[uuid].path for uuid in self.__libraries]
        return res

    """
    Manager operations for managing current library
    """

    def use_library(self, uuid: str) -> bool:
        """Switch to another library with given UUID
        """
        if uuid and uuid in self.__libraries:
            lib: LibInfo = self.__libraries[uuid]
            LOGGER.info(f'Switch to library, name: {lib.name}, UUID: {uuid}')
            if self.__instanize_lib(uuid):
                self.__save()
                return True

        LOGGER.info(f'Switch to library but target not found, UUID: {uuid}')
        return False

    def create_library(self, new_lib: LibInfo, switch_to: bool = False):
        """Add a library to the manager, this only write the library info to config file unless the switch_to flag is set
        - Pre check to params must be done before calling this method
        """
        if new_lib.uuid in self.__libraries or new_lib.path in self.get_library_path_list():
            if new_lib.uuid in self.__libraries and new_lib.path == self.__libraries[new_lib.uuid].path:
                # If the new library's same UUID and and same path all matched, do nothing
                LOGGER.info(
                    f'A library with same UUID and path already exists, name: {new_lib.name}, UUID: {new_lib.uuid}')
            else:
                raise LibraryManagerException('Library with same UUID or path already exists')
        else:
            LOGGER.info(f'Creating new library, name: {new_lib.name}, UUID: {new_lib.uuid}')
            self.__libraries[new_lib.uuid] = new_lib

        if switch_to:
            if self.__instanize_lib(new_lib.uuid):
                self.__save()
        else:
            self.__save()

    def demolish_library(self):
        """Demolish current library
        """
        if not self.instance:
            raise LibraryManagerException('Only an active library can be deleted')

        uuid: str = self.instance.uuid
        LOGGER.warn(f'Ready to demolish library: {self.__libraries[uuid]}')
        self.instance.demolish()
        self.instance = None
        self.__libraries.pop(uuid)
        self.__favorite_list = set()
        self.__save()

    def change_name(self, new_name: str):
        """Change library name for both library instance and the config file of manager
        """
        if not self.instance or not new_name:
            return

        obj: LibInfo | None = self.get_current_lib_info()
        if not obj:
            return

        self.instance.change_lib_name(new_name)
        obj.name = new_name
        self.__save()

    def change_view_style(self, new_style: str):
        """Change view style for both library instance and the config file of manager
        """
        if not self.instance or not new_style:
            return

        obj: LibInfo | None = self.get_current_lib_info()
        if not obj:
            return

        self.instance.change_view_style(new_style)
        self.__save()

    def change_sorted_by(self, new_sorted_by: str):
        """Change sorted by for both library instance and the config file of manager
        """
        if not self.instance or not new_sorted_by:
            return

        obj: LibInfo | None = self.get_current_lib_info()
        if not obj:
            return

        self.instance.change_sorted_by(new_sorted_by)
        self.__save()

    """
    Library operations
    """

    def __instanize_lib(self, lib_uuid: str) -> bool:
        """Build instance for current active library and load library metadata

        Return True if the instanization is succeeded, otherwise False
        """
        if self.instance and self.instance.uuid == lib_uuid:
            return True

        self.instance = None
        if lib_uuid in self.__libraries:
            try:
                obj: LibInfo = self.__libraries[lib_uuid]
                if obj.type == LibTypes.IMAGE.value:
                    self.instance = ImageLib(obj.path, obj.name, obj.uuid, local_mode=True)
                elif obj.type == LibTypes.VIDEO.value:
                    raise LibraryError('Video library is not supported yet')
                elif obj.type == LibTypes.DOCUMENT.value:
                    self.instance = DocumentLib(obj.path, obj.name, obj.uuid)
                elif obj.type == LibTypes.GENERAL.value:
                    raise LibraryError('General library is not supported yet')
                return True
            except Exception as e:
                LOGGER.error(f'Library instanization failed, error: {e}')
                return False
        return False

    def make_library_ready(self, **kwargs) -> str | None:
        """Preheat the library instance to make it workable:
        - If the library is new, it will start initialization and load data
        - If the library is already initialized, it will load saved data to memory directly

        If UUID_EMPTY is returned, it means the library is already ready
        - Otherwise use returned task ID to track the progress of preheat

        Returns:
            str | None: Task ID, UUID_EMPTY if the library is already ready, None for any failure
        """
        if not self.instance:
            raise LibraryManagerException('Library is not selected')

        # Image library case
        if isinstance(self.instance, ImageLib):
            force_init: bool = kwargs.get('force_init', False)
            incremental: bool = kwargs.get('incremental', False)

            # If the library is already ready and not force init & not incremental, do nothing
            if self.instance.is_ready() and not force_init and not incremental:
                return UUID_EMPTY

            self.instance.set_embedder(ImageEmbedder())
            if incremental and not force_init:
                # The phase count is 1 for image library's initialization task
                task_id: str | None = self.task_runner.submit_task(self.instance.incremental_scan, None, True, True, 1)
            else:
                task_id: str | None = self.task_runner.submit_task(self.instance.full_scan, None, True, True, 1,
                                                                   force_init=force_init)
            return task_id

        # Document library case
        if isinstance(self.instance, DocumentLib):
            if not kwargs or 'relative_path' not in kwargs or 'provider_type' not in kwargs \
                    or not kwargs['relative_path'] or not kwargs['provider_type']:
                raise LibraryManagerException(f'Invalid parameters for DocumentLib, kwargs: {kwargs}')

            if self.instance.lib_is_ready_on_current_doc(kwargs['relative_path']):
                return UUID_EMPTY

            relative_path: str = kwargs['relative_path']
            relative_path = relative_path.strip().lstrip(os.path.sep)
            if not relative_path:
                raise LibraryManagerException(f'Invalid parameters for DocumentLib, kwargs: {kwargs}')

            lite_mode: bool = kwargs.get('lite_mode', False)
            self.instance.set_embedder(DocEmbedder(lite_mode=lite_mode))
            # The phase count is 2 for document library's initialization task
            task_id: str | None = self.task_runner.submit_task(self.instance.use_doc, None, True, True, 2,
                                                               relative_path=relative_path,
                                                               provider_type=kwargs['provider_type'],
                                                               force_init=kwargs.get('force_init', False))
            return task_id

        # And more...
        # TODO: Add more library types here

        raise LibraryManagerException('Library type not supported')

    def get_embedding_records(self) -> dict[str, str]:
        """Get all embedding records of current library [relative_path: UUID]
        """
        if not self.instance:
            return dict()

        return self.instance.get_embedded_files()
