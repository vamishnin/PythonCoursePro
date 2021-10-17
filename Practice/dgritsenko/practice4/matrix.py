import sys

def print_matrix(mat):
    if not isinstance(mat, list) or not isinstance(mat[0], list):
        print('not matrix!')
    for line in mat:
        print(line)


def remove_columns(matrix, num):
    column_nums_2_remove = set()
    for line in matrix:
        for idx, val in enumerate(line):
            if val == num:
                column_nums_2_remove.add(idx)

    list_column_nums_2_remove = list(column_nums_2_remove)
    list_column_nums_2_remove.sort()

    for line in matrix:
        decrease_dimension_factor = 0
        for rem_idx in list_column_nums_2_remove:
            del line[rem_idx - decrease_dimension_factor]
            decrease_dimension_factor += 1

matrix = [
    [5, 5, 5, 5, 5, 5, 5, 5, 3],
    [5, 5, 5, 5, 3, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5]
]
print_matrix(matrix)
remove_columns(matrix, 3)
print_matrix(matrix)
