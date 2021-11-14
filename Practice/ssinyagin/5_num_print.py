def numprint(num):
    #numlist = num
    j = 0
    print(f'Число: {num}')
    while j < len(num):
        if num[j].isdecimal():
            print(f'{j + 1} цифра равна {num[j]}')
        else:
            print('Апчхи"')
        j += 1


num = input('Введите 5-значное число: ')
t = numprint(num)3