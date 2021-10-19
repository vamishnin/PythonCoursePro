val = input(f'Введите пятизначное число: ')

def enum(x):
    #Условие для ввода аргумента. Пятизначное число.
    if len(x) == 5 and x.isnumeric():
        for i, j in enumerate(x, start = 1):
            print(f'{i} цифра равна {j}')
    else:
        print(f"Вы указали не пятизначное число")

enum(val)
