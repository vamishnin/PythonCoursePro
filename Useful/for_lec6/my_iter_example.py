class MyIt:
    def __init__(self, n):
        self._n = n
        self._i = 0
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count < self._n:
            t = self._i
            self._i += 2
            self._count += 1
            return t
        else:
            raise StopIteration


# for i in MyIt(10):
#     print(i)

it = iter(MyIt(10))
try:
    while True:
        i = next(it)
        print(i)
except StopIteration:
    pass