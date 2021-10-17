import copy


def multiplier(m=1, source=[1, 2, 3]):
    """
    Как таковых ошибок в этом варианте фукнции нет. Она же работает ;)
    Функция multiplier изменяет source, который подается ей на вход. Скорее всего это нежелательно
    """
    result = source
    for i, x in enumerate(result):
        result[i] *= m
    return result


def multiplier_const(m=1, source=[1, 2, 3]):
    """
    result указывает на новый объект в памяти и функция не изменяет входные данные
    """
    result = copy.deepcopy(source)
    for i, x in enumerate(result):
        result[i] *= m
    return result


def multiplier_short(m=1, source=[1, 2, 3]):
    """
    Возвращается сгенерированный список на основе входного списка
    """
    return [x * m for x in source]


src = [9, 2, 3, 4, 5]
res = multiplier_short(3, src)
print(src)
print(res)
