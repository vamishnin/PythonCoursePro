import sqlite3
import json

class SQLite3:
    def __init__(self, database=':memory:'):
        self._conn = None
        self._cursor = None
        self.open(database)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        if isinstance(exc_val, Exception):
            self._conn.rollback()
        else:
            self._conn.commit()
        self._conn.close()

    def open(self, database):
        try:
            self._conn = sqlite3.connect(database)
            # self._conn.row_factory = sqlite3.Row
            self._cursor = self._conn.cursor()
        except sqlite3.Error as e:
            print(f'Database connection error {e}')

    def execute(self, sql, *args, **kwargs):
        # try:
        self._cursor.execute(sql, *args, **kwargs)
        # except Exception as e:
        #     print(e)

    def select(self, table, fields, limit=None, offset=None):
        """

        :param table: table_name to select fields from
        :type table: str
        :param fields: list of field names delimited by ','
        :type fields: str
        :param limit: result row limit
        :type limit: int
        :param offset: result rows offset
        :type offset: int
        :return: self._cursor.fetchall()
        :rtype: generator
        """

        # выражения вида SELECT :fields from :table_name не поддерживаются библиотекой.
        # использование format для table_name опасно. Если в случае одной таблицы еще можно как-то
        # проверить на корректность имя таблицы, то в случае выборки из нескольких таблиц или
        # выборки составных выражений с использованием значений полей ( field1 || '_' || field2)
        # придётся добавлять парсер SQL по таблицам и/или полям.
        #

        select_stmt = 'SELECT {1} from {0}'.format(table, fields)
        stmt_args = {}

        if isinstance(limit,  int):
            select_stmt += ' LIMIT :limit'
            stmt_args['limit'] = limit
            if isinstance(offset,  int):
                select_stmt += ' OFFSET :offset'
                stmt_args['offset'] = offset

        self.execute(select_stmt, stmt_args)
        return self._cursor.fetchall()

    def select_json(self, table, fields, limit=None, offset=None):
        res = []
        for row in self.select(table, fields, limit, offset):
            res.append({col[0]: row[idx] for idx, col in enumerate(self._cursor.description)})

        return json.dumps(res)

def main():
    table_name = 'my_table'
    create_stmt = "CREATE TABLE if not exists {}(" \
                  "id  integer primary key autoincrement," \
                  "name char(128)," \
                  "surname char(128)" \
                  ")".format(table_name)

    select_stmt = "select * from {}".format(table_name)
    # with SQLite3('test.db') as myconn:
    with SQLite3() as myconn:
        myconn.execute(create_stmt)
        for i in range(20):
            myconn.execute('INSERT INTO {0}(name, surname) VALUES(:name, :surname)'.format(table_name),
                           {'name': f'word{i}', 'surname': f'word{i+10}'})

        print([x for x in myconn.select(table_name, '*',  limit=10,  offset=2)])
        # print([x for x in myconn.select(table_name, 'name', limit=10, offset=2)])
        # print([x for x in myconn.select(table_name, 'surname', limit=10, offset=2)])
        # print([x for x in myconn.select(table_name, 'name',  limit=10,  offset=20)])
        # print([x for x in myconn.select(table_name, 'f1, f2', limit=10)])
        # print([x for x in myconn.select(table_name, 'name, f2', limit=10)])
        # print([x for x in myconn.select(table_name, 'f1, f2')])
        #
        print(myconn.select_json(table_name, '*',  limit=10,  offset=2))

    # with SQLite3('test.db') as myconn:
    with SQLite3() as myconn:
        myconn.execute(create_stmt)
        print('0')
        for i in range(20,25):
            myconn.execute('INSERT INTO {0}(name, surname) VALUES(:name, :surname)'.format(table_name),
                           {'name': f'word{i}', 'surname': f'word{i + 10}'})
        print('1')
        for i in range(20,25):
            myconn.execute('INSERT INTO {0}(name, surname) VALUES(:name, :surname)'.format(table_name),
                           {'name': f'word{i}', 'surname': f'word{i + 10}'})
        print('2')

        myconn.execute("delete from my table where name1='234'")

if __name__ == '__main__':
    main()
