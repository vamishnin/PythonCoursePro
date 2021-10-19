from random import randint

while 1:    # ввод и проверка границ диапазона
    low = input('Введите нижнюю границу: ')
    hight = input('Введите верхнюю границу: ')
    if (low.isdecimal() and hight.isdecimal()) and (int(low) < int(hight)):
        low = int(low)
        hight = int(hight)
        break
    else:
        print(f'Вы ввели некорректный диапазон')


secret = randint(low, hight)

# угадываем число
while 1:
    answer = input('Попытайте удачу, введите число: ')
    if not answer.isdecimal():
        print(f'"{answer}" - это не число')
        break
    answer = int(answer)
    if answer < secret:
        print(f'Попробуйте побольше')
    elif answer > secret:
        print(f'Попробуйте поменьше')
    else:
        print(f'Угадали!')
        break
