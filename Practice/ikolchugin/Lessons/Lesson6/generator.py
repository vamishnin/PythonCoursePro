#
def multiplier(m=1, source=[1, 2, 3]):
    result = source                 # result -  это не новый список, а тот же самый объект список source
    for i, x in enumerate(source):  # зачем то итерируем через enumerate и каждый раз обращаемся к элементу по индексу
        result[i] *= m              # вместо непосредственного обращения к "x"

    return result                   #

# Простейшее исправление, но не самое эффективное.
def multiplier_0(m=1, source=[1, 2, 3]):
    result = source.copy()
    for i, x in enumerate(source):
        result[i] *= m

    return result

# так лучше.
def multiplier_1(m=1, source=[1, 2, 3]):
    result = []
    for x in source:
        result.append(x*m)

    return result

#так еще лучше
def multiplier_iter(m=1, source=[1, 2, 3]):
    return tuple(x*m for x in source)

# а если вдруг понадобится обработать очень большой список и потом когда-нибудь итерировать по результату умножения
# то с генератором не будет тратиться память на хранение результата умножения всех элементов списка,
# как в предыдущих вариантах.
def multiplier_gen(m=1, source=[1, 2, 3]):
    t = None
    for x in source:
        t = x * m
        yield t

# тоже генератор, только проще запись
def multiplier_gen1(m=1, source=[1, 2, 3]):
    return (x * m for x in source)


print(multiplier_iter(5))

m0 = multiplier_gen(5)
print(m0)
print(list(m0))

m1 = multiplier_gen1(5)
print(m1)
print(list(m1))

