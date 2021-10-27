class NewIter:

    def __init__(self, input_container):
        self.__input_container = input_container
        self.element_id = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.element_id += 1
        if self.element_id >= len(self.__input_container):
            raise StopIteration
        return self.__input_container[self.element_id]

    def get_next(self, elements_amount):
        iter_list = []
        el_num = 1
        while el_num <= elements_amount:
            iter_list.append(self.__input_container[self.element_id + el_num])
            el_num += 1
            if self.element_id + el_num >= len(self.__input_container):
                return iter_list

        return iter_list


print('example 1')
lst = NewIter([1, 2, 3, 5, 8, 34, 56, 8])
print(next(lst))
print(lst.get_next(4))
print(next(lst))

print('example 2')
tup = NewIter((3, 5, 7, 8, 23, 45, 9, 80))
try:
    print(next(tup))
    print(next(tup))
    print(tup.get_next(12))
except StopIteration:
    pass

print('example 3')
lst = NewIter([1, 2, 3])
try:
    print(next(lst))
    print(next(lst))
    print(next(lst))
    print(next(lst))
except StopIteration:
    pass
