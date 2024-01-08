from sqlite3 import Cursor

from sqlite.db import SqliteConnection
from sqlite.sql_basic import *
from sqlite.sql_wechat_history import *


class WechatHistoryTable(SqliteConnection):
    def __init__(self, table_name: str):
        self.table_name: str = table_name
        super().__init__(DB_NAME)
        self.__initialize_table()

    def __initialize_table(self) -> None:
        if self.db is None:
            raise ValueError('db is None')

        cursor = self.db.cursor()
        cursor.execute(initialize_table_sql(self.table_name))
        cursor.execute(create_index_sql(self.table_name, 'timestamp'))
        cursor.execute(create_index_sql(self.table_name, 'sender'))
        cursor.execute(create_index_sql(self.table_name, 'reply_to'))
        self.db.commit()

    def insert_row(self, row: tuple) -> int | None:
        if self.db is None:
            raise ValueError('db is None')
        # Skip the first column (id)
        if not row or len(row) != RECORD_LENGTH-1:
            raise ValueError('row size is not correct')

        cur: Cursor = self.db.cursor()
        cur.execute(insert_row_sql(self.table_name), row)
        self.db.commit()
        return cur.lastrowid

    def insert_rows(self, rows: list[tuple]) -> int | None:
        if self.db is None:
            raise ValueError('db is None')
        # Skip the first column (id)
        for row in rows:
            if not row or len(row) != RECORD_LENGTH-1:
                raise ValueError('row size is not correct')

        cur: Cursor = self.db.cursor()
        cur.executemany(insert_row_sql(self.table_name), rows)
        self.db.commit()
        return cur.lastrowid

    def select_row(self, row_id: int) -> tuple | None:
        if self.db is None:
            raise ValueError('db is None')

        cur: Cursor = self.db.cursor()
        cur.execute(select_by_id_sql(self.table_name), (row_id,))
        return cur.fetchone()

    def select_many(self, k: int = -1, order_by: str | None = None) -> Cursor:
        if self.db is None:
            raise ValueError('db is None')

        cur: Cursor = self.db.cursor()
        cmd: str = select_all_sql(self.table_name) if k == -1 else select_many_sql(self.table_name, k)
        cur.execute(cmd)
        return cur

    def clean_all_data(self) -> None:
        if self.db is None:
            raise ValueError('db is None')

        cur: Cursor = self.db.cursor()
        cur.execute(empty_table_sql(self.table_name))
        self.db.commit()
        # Also vacuum the table to reduce file size, as SQLite just mark the rows as deleted
        cur.execute('VACUUM')
        self.db.commit()

    def select_rows_by_sender(self, sender: str) -> Cursor:
        if self.db is None:
            raise ValueError('db is None')

        cur: Cursor = self.db.cursor()
        cur.execute(select_by_sender_sql(self.table_name), (sender,))
        return cur