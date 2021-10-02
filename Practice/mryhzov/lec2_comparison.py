x_glob = int(input('Введите  1е число: '))
y_glob = int(input('Введите  2е число: '))


# Функция сравнивающая два числа и выводящая большее из них

def comp_pint(x_loc, y_loc):
    if x_loc > y_loc:
        print(f'Результат Ф1: Число {x_loc}  - большее')


def comp_pint(x_loc, y_loc):
    if x_loc > y_loc:
        print(f'Число {x_loc}  - большее')
    elif x_loc < y_loc:
        print(f'Результат Ф1: Число {y_loc}  - большее')
    else:
        print('Результат Ф1: Числа одинаковы')


comp_pint(x_glob, y_glob)


# Функция сравнивающая два числа и возвращающая большее число
def comp_return_digit(x_loc, y_loc):
    if x_loc < y_loc:
        a = y_loc
    elif x_loc > y_loc:
        a = x_loc
    else:
        a = None
    return a  #


result1 = comp_return_digit(x_glob, y_glob)

if result1 is None:
    print(f'Результат Ф2: числа одинаковы')
else:
    print(f'Результат Ф2: {result1} - большее')


# Вариант функции с возвращенем значений строками
def comp_return_str(x_loc, y_loc):
    if x_loc < y_loc:
        b = f'Число {y_loc} - большее'
    elif x_loc > y_loc:
        b = f'Число {x_loc} - большее'
    else:
        b = f'Числа одинаковы'
    return b


result2 = comp_return_str(x_glob, y_glob)
print(f'Результат Ф3: {result2}')
