s = ''

while (a := input('Введите числовой символ: ').lower()) != 'stop':
    if a.isdecimal():
        s += a
        print(s)
    else:
        print('Введен нечисловой символ. Введите новый символ.')
