# Ошибка была в отсутсвии выхода из цикла while True
# Из-за ошибки получался бесконечный генератор списка

def chargen():
    while True:  # Лучше удалить этот цикл
        for c in '0123456789':
            yield c
        break  # можно добавить break


words = [c + c for c in chargen()][:10]
print(words)
