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
        self.table_name = (table_name,)

    def connect_and_return_cursor(self):  # noqa: D102,ANN201
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection.cursor()

    def __len__(self):
        self.cursor = self.connect_and_return_cursor()
        self.cursor.execute(f"SELECT count(*) FROM {self.table_name[0]}")  # noqa: S608
        return self.cursor.fetchone()[0]

    def __iter__(self):
        self.cursor = self.connect_and_return_cursor()
        for row in self.cursor.execute(
            f"SELECT * FROM {self.table_name[0]}"  # noqa: S608
        ):  # noqa: S608
            yield row

    def __getitem__(self, item: str):
        item = (item,)
        self.cursor = self.connect_and_return_cursor()
        self.cursor.execute(
            f"SELECT * FROM {self.table_name[0]} WHERE name = '{item[0]}'"  # noqa: S608
        )
        return tuple(self.cursor.fetchone())

    def __contains__(self, item: str):
        item = (item,)
        self.cursor = self.connect_and_return_cursor()
        self.cursor.execute(
            f"SELECT count(*) FROM {self.table_name[0]} WHERE name = '{item[0]}'"  # noqa: S608
        )
        return self.cursor.fetchone()[0] > 0
