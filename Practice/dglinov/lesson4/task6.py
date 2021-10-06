
'''
* Есть список списков (матрица). Каждый внутренний список - это строка матрицы. Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.
'''

matrix = [
    [4, 9, 12],
    [5, 2, 13],
    [6, 11, 4]
]

n = int(input("Введите цифру:" ))
s = set()

for lst in matrix:
    for idx, val in enumerate(lst):
        if val == n:
            s.add(idx)

for x in sorted(s, reverse=True):
    for lst in matrix:
        lst.pop(x)

print(s, matrix)
