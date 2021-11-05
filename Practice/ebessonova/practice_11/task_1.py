# -*- coding: utf-8 -*-
import sqlite3
import json


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
        cursor = self.__conn.execute(sql_req)
        with open('data.json', 'w') as f:
            data_dict = dict()

            for row in cursor:
                i = 0
                data_dict.clear()

                id_is_found = False
                name_is_found = False
                age_is_found = False
                address_is_found = False
                salary_is_found = False

                while i < len(row):
                    if sql_req.find(' id') > 0 and not id_is_found:
                        data_dict.update({'id': row[i]})
                        id_is_found = True
                        i += 1
                        continue
                    if sql_req.find(' name') > 0 and not name_is_found:
                        data_dict.update({'name': row[i]})
                        name_is_found = True
                        i += 1
                        continue
                    if sql_req.find(' age') > 0 and not age_is_found:
                        data_dict.update({'age': row[i]})
                        age_is_found = True
                        i += 1
                        continue
                    if sql_req.find(' address') > 0 and not address_is_found:
                        data_dict.update({'address': row[i]})
                        address_is_found = True
                        i += 1
                        continue
                    if sql_req.find(' salary') > 0 and not salary_is_found:
                        data_dict.update({'salary': row[i]})
                        salary_is_found = True
                        i += 1
                        continue
                    i += 1

                json.dump(data_dict, f)


if __name__ == "__main__":
    conn = sqlite3.connect('new_base.db')
    conn.execute('CREATE TABLE COMPANY'
                        '    (ID       INT   PRIMARY KEY  NOT NULL,'
                        '     NAME     TEXT               NOT NULL,'
                        '     AGE      INT                NOT NULL,'
                        '     ADDRESS  CHAR(50),'
                        '     SALARY   REAL);')
    obj = SQLiteWrapper(conn)
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






