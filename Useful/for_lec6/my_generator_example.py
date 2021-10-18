def gen():
    i = 0
    count = 0
    while count < 10:
        yield i
        i += 2
        count += 1


g = gen()
try:
    while True:
        i = next(g)
        print(i)
except StopIteration:
    pass

