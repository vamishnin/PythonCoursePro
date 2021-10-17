import itertools


a = [1, 2, 3]
b = [4, 5, 6]

c = itertools.chain(a, b)
print(f'{list(c)}')

d = ['hello', 'i', 'write', 'cool', 'code']
e = itertools.filterfalse(lambda x : len(x) < 5, d)
print(f'{list(e)}')

g = 'password'
h = itertools.combinations(g, 4)

res = ''
for i in h:
    res += ''.join(i)
    res += ", "
    
print(res)