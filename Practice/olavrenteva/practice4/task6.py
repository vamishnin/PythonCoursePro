def exclude_column(lst, value):
    for line in lst:
        if value in line:
            index = line.index(value)
            for each in lst:
                each.pop(index)
            exclude_column(lst, value)
    return


matrix = [[1, 15, -10, 2], [3, 2, 4, 100], [17, 16, 15, 0]]
exclude_column(matrix, 2)
print(matrix)
