import itertools

src = ([1, 2, 3], [4, 5], [6, 7])

res = itertools.chain.from_iterable(src)
print(set(res))


src = (['hello', 'i', 'write', 'cool', 'code'])
res = itertools.filterfalse(lambda x: len(x) < 5, src)
print(tuple(res))

src = 'password'
print(tuple(itertools.permutations(src, 4)))
