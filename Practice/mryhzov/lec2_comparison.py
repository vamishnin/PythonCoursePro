x_glob = int(input('Введите  1е число: '))
y_glob = int(input('Введите  2е число: '))


# Функция сравнивающая два числа и выводящая большее из них
def comp_pint(x_loc, y_loc):     # 0. объявили функцию
    if x_loc > y_loc:            # 2. сравнениваем переданные значения аргументов и выводим большее из них
        print(f'Число {x_loc}  - большее')
    elif x_loc < y_loc:
        print(f'Число {y_loc}  - большее')
    else:
        print('Числа одинаковы')


comp_pint(x_glob, y_glob)         # 1. вызвали функцию задав значения ее аргументов x_glob, y_glob


# Функция сравнивающая два числа и возвращающая большее из них
def comp_return(x_loc, y_loc):    # 0. объявили функцию
    if x_loc > y_loc:             # 2. сравниваем числа
        a = x_loc                 # 3. результат сравнения обозначаем переменной 'a'
    elif x_loc < y_loc:
        a = y_loc
    else:
        a = 'числа одинаковы'
    return a    # 4. возвращаем результат выполнения функции в глобальное пространство


result = comp_return(x_glob, y_glob)   # 1. вызываем функцию и присваиваем результат ее выполнения переменной result
if result == 'числа одинаковы':        # 5. выводим результат  в глобальном пространстве
    print(f'Результат: {result}')
else:
    print(f'Результат: {result} - большее')
