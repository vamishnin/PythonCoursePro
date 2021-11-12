d = True
b = ''
while d:
    a = input('Введите число: ')
    if a.lower() == 'stop':
        print(b)
        d = False
    elif a.isdecimal():
        b = b + a
    else:
        print('ALARM! введите числовой символ')
