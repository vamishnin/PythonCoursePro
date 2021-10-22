class NewIter:

    def __init__(self, input_container):
        self.__input_container = iter(input_container)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__input_container)

    def get_next(self, elements_amount):
        iter_list = []
        el_num = 0
        try:
            while el_num < elements_amount:
                iter_list.append(next(self.__input_container))
                el_num += 1
        except StopIteration:
            print(f'Elements amount is bigger then sequence length, only {el_num} returns')

        return iter_list


lst = NewIter([1, 2, 3, 5, 8, 34, 56, 8])
print(next(lst))
print(next(lst))
print(lst.get_next(4))

tup = NewIter((3, 5, 7, 8, 23, 45, 9, 80))
print(next(tup))
print(next(tup))
print(tup.get_next(12))

lst = NewIter([1, 2, 3])
try:
    print(next(lst))
    print(next(lst))
    print(next(lst))
    print(next(lst))
except StopIteration:
    pass
