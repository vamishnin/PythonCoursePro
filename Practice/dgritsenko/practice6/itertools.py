import itertools


def merge_lists(l1, l2, l3):
    if any((not isinstance(x, list)) for x in (l1, l2, l3)):
        print("Bad input data!")
        return
    return list(itertools.chain(l1, l2, l3))


def custom_drop_while(input_arr):
    return itertools.filterfalse(lambda x: len(x) < 5, input_arr)


def custom_permutation(input_str):
    if not isinstance(input_str, str):
        print("Bad input data!")
        return
    return itertools.permutations(input_str, 4)


print(merge_lists([1, 2, 3], [4, 5], [6, 7]))
print(list(custom_drop_while(['hello', 'i', 'write', 'cool', 'code'])))
print(list(custom_permutation('password')))
