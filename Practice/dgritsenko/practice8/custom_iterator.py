

class Iterator:
    def __init__(self, list):
        self._i = 0
        self._list = list

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._list):
            self._i += 1
            return self._list[self._i - 1]
        else:
            raise StopIteration

    def show_next(self, num=1):
        print(self._list[self._i : self._i + min(num, len(self._list) - self._i)])


data = [1,2,3,4,5]
it = Iterator(data)
print(next(it))
print(next(it))
it.show_next(2)
it.show_next(10)