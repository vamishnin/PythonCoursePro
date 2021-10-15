d = True
l = ('stop', "Stop", 'STOP')
b = 0
while d is True:
    a = input('Введите число: ')
    try:
        c = int(a)
        b += c
    except:
        if a in l:
            n = int(b)
            print(f'{n}')
            d = False
        else:
            print('ALARM! введите числовой символ')
