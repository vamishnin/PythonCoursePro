matrix = [[1, 2, 3, 4],
          [3, 5, 7, 9],
          [1, 4, 5, 2]]

elem_del = input('Input element for deletion: ')
# найдем номера колонок, которые нужно удалить
lst_del = set()
for lst in matrix:
    j = 0
    for elem in lst:
        if elem == int(elem_del):
            lst_del.add(j)
        j += 1

# последовательно удаляем элементы из каждой строки с конца
for lst in matrix:
    for col in reversed(list(lst_del)):
        lst.pop(col)

print('Result matrix:')
for lst in matrix:
    print(lst)

