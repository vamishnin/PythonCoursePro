def max_num():
    #Создаем пустой список
    list = []
    #Просим пользователя ввести 2 числа и добавляем их в созданный список
    a = input("Введите первое число: ")
    b = input("Введите первое число: ")
    list.append(a)
    list.append(b)
    print(max(list), "- наибольшее из двух чисел")

def more_num(a, b):
    if a > b:
        return a
    else:
        return b