# Составить программу, которая будет считывать введённое пятизначное число.

while 1:    # Валидация
    num = input('Введите 5-значное число: ')
    if not num.isdecimal():
        print('Вы ввели не число')
    elif len(num) != 5:
        print('Вы ввели некорректное число')
    else:
        break

number = 1
for i in num:
    print(f'{number} цифра равна {i}')
    number += 1
