def multiplier(m=1, source=(1, 2, 3)):
    return [x * m for x in source]


print(multiplier(10, (3, 6, 7)))
print(multiplier(5))
print(multiplier(5))
