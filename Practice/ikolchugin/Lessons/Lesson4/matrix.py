from random import shuffle, randrange

# Размер матрицы
M = N = 5


def create_matrix(size_x=M, size_y=N):
    _matrix = [list(range(M)) for _ in range(N)]
    for i in _matrix:
        shuffle(i)
    return _matrix


def create_anomaly(matrix):
    _anomaly = randrange(0, 70)
    matrix[randrange(1, M)][randrange(1, N)] = _anomaly
    return _anomaly


def find_columns(_matrix, _val):
    _columns = set()

    for row in _matrix:
        i = 0
        for col in row:
            if col == _val:
                _columns.add(i)
            i += 1

    return _columns


def del_columns(_matrix, _columns):
    rev_columns = tuple(sorted(_columns, reverse=True))

    for row in _matrix:
        i = 0
        for col in rev_columns:
            del row[col]


def print_matrix(_matrix):
    for i in _matrix:
        print(i)


matrix = create_matrix()
anomaly = create_anomaly(matrix)
anomaly = create_anomaly(matrix)

print_matrix(matrix)

while not (len(x := input('Введите число: ')) > 0 and x.isdigit()):
    pass
anomaly = int(x)

columns = find_columns(matrix, anomaly)
print(f'Удалить столбцы {columns} с числом {anomaly}')
del_columns(matrix, columns)

print_matrix(matrix)