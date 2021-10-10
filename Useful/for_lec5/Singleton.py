class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls, *args, **kwargs)
        return cls.obj


s1 = Singleton()
s2 = Singleton()
assert(id(s1)==id(s2))  # True