mtx = [[1, 2, 3, 4], [5, 66, 7, 8], [9, 10, 11, 12], [32, 55, 66, 77]]


print(mtx)


def del_col(matrix: list, val_to_del: int):
    rows = len(matrix)
    for i in matrix:
        if val_to_del in i:
            z = i.index(val_to_del)
            for n in range(rows):
                matrix[n].pop(z)
    return matrix


del_col(mtx, 10)

print(mtx)
