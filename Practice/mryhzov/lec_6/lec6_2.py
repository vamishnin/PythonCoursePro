def multiplier(m=1, source=[1, 2, 3]):
    mul_source = [i * m for i in source]    # списковое выражение
    return mul_source


mul_list1 = multiplier()
mul_list2 = multiplier(5, [10, 20, 30])
print(mul_list1)
print(mul_list2)

