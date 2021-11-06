# -*- coding: utf-8 -*-
import sqlite3
import json
import os


class SQLiteWrapper:
    def __init__(self, conn):
        self.__conn = conn

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.__conn.close()

    def execute(self, sql_req):
        self.__conn.execute(sql_req)
        self.__conn.commit()

    def select(self, sql_req):
        self.__conn.row_factory = sqlite3.Row  # позволяет возвращать в т.ч. и названия полей
        cursor = self.__conn.execute(sql_req)
        with open('data.json', 'w') as f:
            for row in cursor:
                json.dump(dict(row), f)  # row нужно преобразовать в dict, чтоб можно было сериализовать в json


def configure_db(connection_db):
    cur = connection_db.cursor()
    cur.execute('CREATE TABLE COMPANY'
                '    (ID       INT   PRIMARY KEY  NOT NULL,'
                '     NAME     TEXT               NOT NULL,'
                '     AGE      INT                NOT NULL,'
                '     ADDRESS  CHAR(50),'
                '     SALARY   REAL);')


if __name__ == "__main__":
    db_name = 'new_base.db'
    db_exists = os.path.exists(db_name)
    conn = sqlite3.connect(db_name)
    obj = SQLiteWrapper(conn)

    if not db_exists:
        configure_db(conn)
        obj.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
                    "VALUES (1, 'Paul', 32, 'California', 20000.00)")
        obj.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
                    "VALUES (2, 'Allen', 25, 'Texas', 15000.00)")
        obj.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
                    "VALUES (3, 'Teddy', 23, 'Norway', 20000.00)")
        obj.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
                    "VALUES (4, 'Mark', 25, 'Richmond', 65000.00)")

    obj.select('SELECT id, name, address, salary from '
               'COMPANY WHERE id = 1 OR id = 2 OR id = 4')






