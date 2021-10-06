'''
Лекция №3 задание 2 "Пятизнак"
'''
while not (len(i := input('Введите пятизначное число: ')) == 5 and i.isdigit()):
    pass
print(f'Число: {i}')
current_number = 1
for n in i:
    print(f'{current_number} цифра равна {n}')
    current_number += 1
