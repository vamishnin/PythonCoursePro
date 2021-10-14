import itertools

#task 1
lst1 = [1, 2, 3]
lst2 = [4, 5]
lst3 = [6, 7]

out_lst = itertools.chain(lst1, lst2, lst3)

print(list(out_lst))


#task 2
lst4 = ['hello', 'i', 'write', 'cool', 'code']

out_lst1 = itertools.filterfalse(lambda elem: len(elem) < 5, ['hello', 'i', 'write', 'cool', 'code'])

print(list(out_lst1))


#task 3
in_str = 'password'

out_lst2 = itertools.combinations_with_replacement(in_str, 4)

print(list(out_lst2))
