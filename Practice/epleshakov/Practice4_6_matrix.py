mtx = [[1, 2, 3, 6, 15, 2, 50], [5, 66, 7, 8, 44, 3, 4], [9, 10, 11, 12, 55, 33, 2], [32, 2, 2, 77, 22, 66, 34]]
mtx2 = [
    [1, 2, 2],
    [5, 66, 7],
    [9, 10, 11]
]

print(mtx)
print(mtx2)


def del_col(matrix: list, val_to_del: int):
    cols_to_del = []
    for n in matrix:
        z = 0
        while z < len(n):
            if n[z] == val_to_del:
                cols_to_del.append(z)
            z += 1
    cols_to_del = list(set(cols_to_del))[::-1]
    for items in matrix:
        for nn in cols_to_del:
            items.pop(nn)
    return matrix


del_col(mtx, 2)
del_col(mtx2, 2)
print(mtx)
print(mtx2)
