def numprint(num):
    numlist = list(num)
    j = 0
    print(f'Число: {num}')
    while j <= len(numlist) - 1:
        try:
            k = int(numlist[j])
            print(f'{(j + 1)} цифра равна {numlist[j]}')
        except ValueError:
            print('Апчхи!')
        j += 1


num = input('Введите 5-значное число: ')
t = numprint(num)