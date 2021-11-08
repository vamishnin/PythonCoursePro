import sqlite3
import json


class SuperSQLite:

    def __init__(self, file: str):
        self.__file = file

    def __enter__(self):
        self.__conn = sqlite3.connect(self.__file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__conn.close()
        
    def select(self, rest_query, *args: dict, output='json'):
        if output == 'json' or output == 'dict':
            self.__conn.row_factory = self.dict_factory
        else:
            self.__conn.row_factory = None
        cur = self.__conn.cursor()
        cur.execute('SELECT ' + rest_query, *args)
        res = cur.fetchall()
        cur.close()
        if output == 'json':
            return json.dumps(res, sort_keys=True, indent=4)
        else:
            return res

    def execute(self, query: str, *args: dict):
        cur = self.__conn.cursor()
        cur.execute(query, *args)
        self.__conn.commit()
        cur.close()

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
        

def fill_in_db(db: SuperSQLite):
    db.execute("""CREATE TABLE IF NOT EXISTS Users
                  (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,
                   Name      CHAR(128)  NOT NULL,
                   Age       INTEGER    NOT NULL)""")
    db.execute("""INSERT OR REPLACE INTO Users (Id, Name, Age) VALUES
        ((SELECT Id FROM Users WHERE Name = :name), :name, :age)""", {'name': 'Petya', 'age': 22})
    db.execute("""INSERT OR REPLACE INTO Users (Id, Name, Age) VALUES
        ((SELECT Id FROM Users WHERE Name = :name), :name, :age)""", {'name': 'Vasya', 'age': 33})
    db.execute("""INSERT OR REPLACE INTO Users (Id, Name, Age) VALUES
        ((SELECT Id FROM Users WHERE Name = :name), :name, :age)""", {'name': 'Fedya', 'age': 44})
    # db.execute("""INSERT OR REPLACE INTO Users (Id, Name, Age) VALUES
    #     ((SELECT Id FROM Users WHERE Name = 'Petya'), 'Petya', 22)""")
    # db.execute("""INSERT OR REPLACE INTO Users (Id, Name, Age) VALUES
    #     ((SELECT Id FROM Users WHERE Name = 'Vasya'), 'Vasya', 33)""")
    # db.execute("""INSERT OR REPLACE INTO Users (Id, Name, Age) VALUES
    #     ((SELECT Id FROM Users WHERE Name = 'Fedya'), 'Fedya', 44)""")


if __name__ == "__main__":
    with SuperSQLite('Practice/akolosov/my_db.db') as db:
        fill_in_db(db)
        print(db.select(' * FROM Users'))
        print(db.select(' * FROM Users', output='dict'))
        print(db.select(' * FROM Users WHERE Name != :name', {'name': 'Qqqq'}, output='tuple'))
