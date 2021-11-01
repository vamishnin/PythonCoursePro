from random import randint


class MyIterator:
    def __init__(self, _my_list):
        self._i = 0
        self._list = _my_list

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._list):
            res = self._list[self._i]
            self._i += 1
            return res
        else:
            raise StopIteration

    def show_next(self, num=1):
        return self._list[self._i:self._i + min(num, len(self._list))]


my_list = [randint((i*10),(i+1)*10) for i in range(20)]

print(my_list)
myiter = MyIterator(my_list)

print(next(myiter))
print(myiter.show_next(4))
print(next(myiter))
print(myiter.show_next(7))
print(next(myiter))

