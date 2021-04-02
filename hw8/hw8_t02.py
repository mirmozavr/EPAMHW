"""
Task.

Write a wrapper class TableData for database table, that when initialized with database name and
table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
 -  `len(presidents)` will give current amount of rows in presidents table in database
 -  `presidents['Yeltsin']` should return single data row for president with name Yeltsin
 -  `'Yeltsin' in presidents` should return if president with same name exists in table
 -  object implements iteration protocol. i.e. you could use it in for loops::
       for president in presidents:
           print(president['name'])
 - all above mentioned calls should reflect most recent data.
 If data in table changed after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory.
 When iterating through records, start reading the first record, then go to the next one,
  until records are exhausted.
When writing tests, it's not always necessary to mock database calls completely.
 Use supplied example.sqlite file as database fixture file.
"""

import sqlite3


class TableData:
    def __init__(self, db_path: str, table_name: str):
        self.db_path = db_path
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # noqa: ANN001
        self.connection.cursor().close()
        self.connection.close()

    def __len__(self):
        self.cursor.execute(f"SELECT count(*) FROM {self.table_name}")  # noqa: S608
        return self.cursor.fetchone()[0]

    def __iter__(self):
        yield from self.cursor.execute(
            f"SELECT * FROM {self.table_name}"  # noqa: S608
        )  # noqa: S608

    def __getitem__(self, item: str):
        self.cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE name = ?", (item,)  # noqa: S608
        )
        return tuple(self.cursor.fetchone())

    def __contains__(self, item: str):
        self.cursor.execute(
            f"SELECT count(*) FROM {self.table_name} WHERE name = ?",  # noqa: S608
            (item,),
        )
        return self.cursor.fetchone()[0] > 0

    def close(self) -> None:
        self.connection.cursor().close()
        self.connection.close()
