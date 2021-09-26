def compare(a, b):
    if a > b:
        res = a
    else:
        res = b
    return res


x = input('Введите первое число: ')
y = input('Введите второе число: ')

print(compare(x, y))
