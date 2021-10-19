import itertools

# Practice 6 Q4_1 - 4_3
it1_arr = [1, 2, 3], [4, 5], [6, 7]
it2_arr = ['hello', 'i', 'write', 'cool', 'code']
it3_str = 'password'


def itertest1(*args):
    return list(itertools.chain.from_iterable(*args))


def itertest2(*args):
    return list(itertools.filterfalse(lambda x: len(x) < 5, *args))


def itertest3(*args):
    return itertools.permutations(*args, len(*args))


# В обратном порядке чтобы поместилось в выводе
for p in itertest3(it3_str):
    print(p)

print(itertest2(it2_arr))
print(itertest1(it1_arr))