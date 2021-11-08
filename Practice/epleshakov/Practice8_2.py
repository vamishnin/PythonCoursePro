# Реализовать итератор с возможностью просмотра следующего элемента
# или набора элементов не меняя состояние итератора.

class Iterate:
    def __init__(self, iter_val):
        self._val = iter_val
        self._next_values = []
        self._n = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._n += 1
        if self._n < len(self._val):
            return self._val[self._n]
        else:
            raise StopIteration

    def nex_val(self, val_col: int):
        self._next_values = self._val[self._n + 1:self._n + val_col + 1]
        return self._next_values


l1 = [3, 1, 2, 5, 8, 2, 4, 2, 3, 1]
l2 = ['odin', 'dva', 'tri', 'tri', 'dva', 'dva', 'chetyre', 'chetyre', 'dva', 'dva']
aa = Iterate(l1)
bb = Iterate(l2)

for ii in aa:
    print(ii)
    print(f'{aa.nex_val(3)=}')
for ii in bb:
    print(ii)
    print(f'{bb.nex_val(3)=}')

# print(next(aa))
# print(next(aa))
# print(next(aa))
# print(next(aa))
# print(f'{aa.nex_val(10)=}')
