import os
from sqlite3 import Cursor
from typing import Callable, Generic, Type, TypeVar

from db.sqlite.table import SqliteTable

# Generic type for SqliteTable
T = TypeVar('T', bound=SqliteTable)


class DocProviderBase(Generic[T]):
    """The basic abstract for an organized document management, it reads raw documents and provides functionalities to organize them
    """

    # Type for the table for this type of document provider
    TABLE_TYPE: type = SqliteTable
    # Lambda function to extract the text to be embedded from a tuple of a row
    EMBED_LAMBDA: Callable[['DocProviderBase', tuple], str] = lambda self, x: ''
    # Lambda function to extract the text to be re-ranked from a tuple of a row
    RERANK_LAMBDA: Callable[['DocProviderBase', tuple], str] = lambda self, x: ''

    def __init__(self,
                 db_file: str,
                 table_name: str,
                 doc_path: str | None,  # Just for Python's generic type param compatibility, not used in base class
                 re_dump: bool,  # Just for Python's generic type param compatibility, not used in base class
                 table_type: Type[T]):
        """Base class for document provider

        Args:
            db_file (str | None): _description_
            table_name (str): _description_
            table_type (Type[T]): Generic type constructor for SqliteTable
        """
        self.table: T = table_type(db_file, table_name)

    def initialize(self, file_path: str):
        """Initialize the document provider, it reads all lines from given file and insert them into the table after some processing
        """
        raise NotImplementedError()

    def get_record_by_id(self, id: int) -> tuple | None:
        """Get one line/segment of a document by ID
        """
        row: tuple | None = self.table.select_row(id)
        return row

    def get_all_records(self) -> list[tuple]:
        """Get all lines/segments
        """
        cursor: Cursor = self.table.select_many()
        rows: list[tuple] | None = cursor.fetchall()
        if not rows:
            return list()
        return rows

    def get_record_count(self) -> int:
        """Get the number of lines/segments of the document
        """
        return self.table.row_count()

    def get_records_by_column(self, **kwargs) -> list[tuple]:
        """Get lines/segments by specific columns defined in the table
        """
        raise NotImplementedError()

    def delete_table(self):
        """Remove current document's table from DB
        """
        self.table.drop_table()

    @staticmethod
    def delete_db_file(db_file: str):
        """Delete the DB file, this will remove all tables in the DB
        """
        if os.path.isfile(db_file):
            os.remove(db_file)