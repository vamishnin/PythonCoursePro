import sqlite3

class MySqlWrapper:

    def __init__(self):
        self._conn = sqlite3.connect('sqlite.db')

    def __enter__(self):
        self._conn.execute(  'CREATE TABLE COMPANY'
                             '    (ID       INT   PRIMARY KEY  NOT NULL,'
                             '     NAME     TEXT               NOT NULL,'
                             '     AGE      INT                NOT NULL,'
                             '     ADDRESS  CHAR(50),'
                             '     SALARY   REAL);')
        print('Таблица создана')

    def __exit__(self):
        self._conn.execute('DROP TABLE COMPANY')
        print('Таблица удалена')

        self._conn.close()


if __name__ == '__main__':
    with MySqlWrapper():
        pass
