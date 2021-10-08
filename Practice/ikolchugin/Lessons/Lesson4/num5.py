while not (len(x := input('Введите 5-значное число: ')) == 5
           and x.isdigit()):
    pass

print(f'Число: {x}')

i = 1
for s in x:
    print(f'{i} цифра равна {s}')
    i += 1
