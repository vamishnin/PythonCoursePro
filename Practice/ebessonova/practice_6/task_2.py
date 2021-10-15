def multiplier(m=1, source=(1, 2, 3)):
    return [x * m for i, x in enumerate(source)]


print(multiplier(10, (3, 6, 7)))
print(multiplier(5))
