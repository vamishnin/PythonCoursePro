class Singleton(type):
    _obj = None

    def __call__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._obj


class DBConnection(metaclass=Singleton):
    _db_name = None

    def __init__(self, db_name):
        if self._db_name is None:
            self._db_name = db_name
            print(f"Connection to {self._db_name} established")


d1 = DBConnection('db_1')
d2 = DBConnection('db_2')
assert id(d1) == id(d2)
