def read_num(a):
    p = 0
    if not a.isdecimal() or len(a) != 5:
        print('Введено некорректное значение')
    else:
        for i in a:
            p += 1
            print(f'{p} цифра равна {i}')


x = input('Введите пятизначное число: ')
read_num(x)