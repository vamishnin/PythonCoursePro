import random

def cheking(mass):
    try:
        #mass_list = list(mass)
        #print(mass_list)
        expect_num = int(random.choice(mass.split()))
#        print(expect_num)
    except ValueError:
        print('Введеный массив некорректен: есть не числа. Запустите программу еще раз, введя числа.')
        return
    while True:
        try:
            guess_num = int(input('Какое число из массива загадала программа? введите его: '))
            if guess_num == expect_num:
                print('Вы угадали! Т.Т')
                return
            else:
                if guess_num < expect_num:
                    print('загаданное чилсо больше ;-)')
                else:
                    print('загаданное чилсо меньше ;-)')
        except ValueError:
            print('Вы ввели не число. Мы так не играем :-(')
            return


mass = input('Введите через пробел массив чисел: ')
res = cheking(mass)
