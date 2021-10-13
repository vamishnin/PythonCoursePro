class Singleton:
    _obj = None

    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = super().__new__(cls, *args, **kwargs)
        return cls._obj


s1 = Singleton()
s2 = Singleton()
assert(id(s1) == id(s2))  # True
