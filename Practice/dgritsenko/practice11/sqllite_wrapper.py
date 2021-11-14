import sqlite3 as sqlite
import json

DB_NAME = 'library.db'


class MySqlWrapper:

    def __init__(self):
        self._insert_id = 0
        self._conn = sqlite.connect(DB_NAME)
        # self._conn.row_factory = sqlite.Row
        self._cursor = self._conn.cursor()

    def __enter__(self):
        self._conn.execute(  'CREATE TABLE BOOKS'
                             '    (ID           INT     PRIMARY KEY  NOT NULL,'
                             '     TITLE        TEXT    NOT NULL,'
                             '     AUTHOR       INT     NOT NULL);')
        print('Таблица создана')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.execute('DROP TABLE BOOKS')
        self._conn.close()
        print('Таблица удалена')

    def execute(self, query, params=None):
        if params:
            self._cursor.execute(query, params)
        else:
            self._cursor.execute(query)
        self._conn.commit()

    def select_books_with_author(self, author):
        self._cursor.execute("SELECT * FROM BOOKS WHERE BOOKS.AUTHOR = :book_author",
                             {'book_author': author})
        res = self._cursor.fetchall()
        return json.dumps(res)

    def insert_book(self, title, author):
        query = "INSERT INTO BOOKS (ID, TITLE, AUTHOR) VALUES (:id, :title, :author)"
        params = {'id': self._insert_id, 'title': title, 'author': author}
        self.execute(query, params)
        self._insert_id += 1


if __name__ == '__main__':
    db = MySqlWrapper()
    with db:
        db.insert_book('Garry Potter 1', 'J. K. Rowling')
        db.insert_book('Garry Potter 2', 'J. K. Rowling')
        db.insert_book('Garry Potter 3', 'J. K. Rowling')
        db.insert_book('Garry Potter 4', 'J. K. Rowling')
        db.insert_book('Garry Potter 5', 'J. K. Rowling')
        db.insert_book('The Idiot', 'Fyodor Dostoevsky')

        data = db.select_books_with_author('Fyodor Dostoevsky')
        print(data)
        data = db.select_books_with_author('J. K. Rowling')
        print(data)
