import collections
import os
from typing import Any
import sqlite3
import json


class DB:
    def __init__(self, conn: Any) -> None:
        self.__conn = conn

    def __enter__(self):
        return self

    def __exit__(self, *args: Any):
        self.__conn.close()

    def create_table(self, query: str):
        cur = self.__conn.cursor()
        cur.execute(query)

    def insert(self, query: str):
        cur = self.__conn.cursor()
        cur.execute(query)
        self.__conn.commit()

    def select(self, query: str) -> json:
        cur = self.__conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        row_list = []
        for row in data:
            r = collections.OrderedDict()
            r['id'] = row[0]
            r['Name'] = row[1]
            r['Age'] = row[2]
            r['Phone'] = row[3]
            row_list.append(r)
            json_db = json.dumps(row_list)
        return json_db


if __name__ == '__main__':
    DB_NAME = 'database.db'
    DB_EXIST = os.path.exists(DB_NAME)
    connect = sqlite3.connect(DB_NAME)
    connect.row_factory = sqlite3.Row
    CREATE_TABLE = 'CREATE TABLE PATIENTS (Id INTEGER PRIMARY KEY AUTOINCREMENT, NAME CHAR(128) NOT NULL, AGE CHAR(64) NOT NULL, PHONE CHAR(64) DEFAULT 0)'
    INSERT_1 = 'INSERT INTO PATIENTS (NAME, AGE, PHONE) VALUES ("Ivanov", "17", "89038889090")'
    INSERT_2 = 'INSERT INTO PATIENTS (NAME, AGE, PHONE) VALUES ("Petrov", "25", "89038886060")'
    SELECT = 'SELECT * FROM Patients'
    with DB(connect) as db:
        db.create_table(CREATE_TABLE)
        db.insert(INSERT_1)
        db.insert(INSERT_2)
        print(db.select(SELECT))