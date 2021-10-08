"""
* Есть список списков (матрица). Каждый внутренний список - это строка матрицы.
Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.
"""
import random


def generator(h, w, start=0, end=100):
    return [[random.randint(start, end) for j in range(w)] for i in range(h)]


def printer(array):
    for line in array:
        print(*line, sep='   ')


if __name__ == '__main__':
    try:
        h = int(input("Rows: "))
        w = int(input("Columns: "))
        mat = generator(h, w)
        printer(mat)
        ids = []
        x = int(input("Enter the number you want to remove: "))
    except ValueError:
        print("Wrong values. Exiting.")
        exit(1)

    for i in mat:
        if x in i:
            # print(f"x={x} in line {i}")
            ids.append(i.index(x))

    if ids:
        for i in ids:
            for row in mat:
                row.pop(i)
    else:
        print(f"There is no {x} in array. Exiting")
        exit(0)

    printer(mat)
