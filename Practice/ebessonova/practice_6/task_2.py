def multiplier(m=1, source=[1, 2, 3]):
    return [source.copy()[i] * m for i, x in enumerate(source)]


print(multiplier(10, [3, 6]))
print(multiplier(5))
