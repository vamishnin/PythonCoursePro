# Создаем класс: Base.__new__ -> type.__new__
# Создаем экземпляр класса: Base.__call__ -> type.__call__ -> class.__new__ -> obj.__init__

class Base(type):
    _obj = None

    def __new__(cls, *args, **kwargs):
        print('new of Base called')
        return super().__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('call of Base called')
        if cls._obj is None:
            cls._obj = super(Base, cls).__call__(*args, **kwargs)
        return cls._obj


class MyClass(metaclass=Base):
    def __new__(cls, *args, **kwargs):
        print('new of MyClass called')
        return super().__new__(cls, *args, **kwargs)


print("start")
ex1 = MyClass()
print("___1")
ex2 = MyClass()
print("___2")
print(f"{id(ex1)=}")
print(f"{id(ex2)=}")

