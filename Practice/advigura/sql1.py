import sqlite3

class SQLLiteWrapper:
        
    def __enter__(self):
        self._db_name = "example.db"
        self._conn = sqlite3.connect(self._db_name)
        self._conn.row_factory = sqlite3.Row 
        self._cur = self._conn.cursor()
        return self
        
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
    
    def select(self, *args):
        self._cur.execute(*args)
        for row in self._cur.fetchall():
            return dict(row)
    
    def execute(self, *args):
        res = self._cur.execute(*args)
        for row in self._cur.fetchall():
            return dict(row)
        
     
     
with SQLLiteWrapper() as myDB:
    myDB.execute("CREATE TABLE IF NOT EXISTS Employees"
                "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name      CHAR(128)  NOT NULL,"
                "     Login     CHAR(16)   NOT NULL,"
                "     Password  CHAR(16)   NOT NULL)")
    myDB.execute('INSERT INTO Employees (Name, Login, Password) VALUES (:name, :login, :password)',
                 {'name': 'Ivan', 'login': 'Ivan5', 'password': '1234'})
    
    print(f"{myDB.select('SELECT * from Employees')}")
    


