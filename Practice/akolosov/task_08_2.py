import copy
import inspect


class MetaIterator:

    def __new__(cls, *args, **kwargs):
        if hasattr(args[0], '__iter__') and not inspect.isgenerator(args[0]):
            return super().__new__(cls)
        else:
            return None

    def __init__(self, arg):
        self.__arg = arg

    def __iter__(self):
        self.__iterator = iter(self.__arg)
        return self.__iterator

    def get_in_advance(self, number: int):
        it = copy.deepcopy(self.__iterator)
        lst = []
        i = 0
        for item in it:
            lst.append(item)
            i += 1
            if i >= number:
                break
        return lst


if __name__ == "__main__":
    cl = MetaIterator(range(1, 10))
    print(MetaIterator(1))
    print(cl)
    it = iter(cl)
    print(f"Iterator: {next(it)} {next(it)} {next(it)}")
    print(f"In advance 2 items: {cl.get_in_advance(2)}")
    print(f"Iterator: {next(it)} {next(it)} {next(it)}")
    print(f"In advance 10 items: {cl.get_in_advance(10)}")
