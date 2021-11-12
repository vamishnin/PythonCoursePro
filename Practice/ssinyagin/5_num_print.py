def numprint(num):
    numlist = num
    j = 0
    print(f'Число: {num}')
    while j < len(numlist):
        if numlist[j].isdecimal():
            print(f'{j + 1} цифра равна {numlist[j]}')
        else:
            print('Апчхи"')
        j += 1


num = input('Введите 5-значное число: ')
t = numprint(num)