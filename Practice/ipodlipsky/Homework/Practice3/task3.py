#
while True:
    res = input(f"Введите число:")
    if res.lower() == 'stop':
        print(f'Конец работы программы. ')
        break
    if res.isdigit():
        print(f'Вы ввели: {res}')
    else:
        print(f'Вы указали нечисловой символ!')