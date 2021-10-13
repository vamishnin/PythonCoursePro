import random


def guess(a):
    while True:
        x = input()
        if not x.isdecimal():
            print('Должно быть введено целое число')
            break
        elif int(x) > a:
            print('Введенное число больше загаданного')
        elif int(x) < a:
            print('Введенное число меньше загаданного')
        else:
            print('Вы угадали!')
            break


upper_num = input('Введите нижнюю границу диапазона: ')
lower_num = input('Введите верхнюю границу диапазона: ')
num = random.randint(int(upper_num), int(lower_num))
print('Угадайте, какое целое число я загадал из выбранного Вами диапазона')

guess(num)
