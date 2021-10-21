class MyIterator:
    def __init__(self, start, num):
        self._num = num
        self._start = start
        self._step = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self._step < self._num:
            self._step += 1
            return self._start + self._step * 3
        else:
            raise StopIteration

    def show_next(self, num=1):
        res = []
        for i in range(1, min(num, self._num - self._step) + 1):
            res.append(self._start + (self._step + i) * 3)
        return res


myiter = MyIterator(10, 5)
print(next(myiter))
print(next(myiter))
print(myiter.show_next(4))
print(next(myiter))

