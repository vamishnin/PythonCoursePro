matrix = [[1, 2, 3, 4],
          [3, 5, 7, 9],
          [1, 4, 5, 2]]

elem_del = input('Input element for deletion: ')
# найдем номера колонок, которые нужно удалить
lst_del = []
for lst in matrix:
    j = 0
    for elem in lst:
        if elem == int(elem_del):
            lst_del.append(j)
        j += 1

# отсортируем список колонок по убыванию,
# чтобы при уменьшении длины строки не менялась индексация колонок
lst_del.sort(reverse=True)
# исключаем повторяющиеся элементы
lst_del = set(lst_del)

# new_lst_del = []
# for el in lst_del:
#     if el not in new_lst_del:
#         new_lst_del.append(el)

# последовательно удаляем элементы из каждой строки
for lst in matrix:
    for col in lst_del:
        lst.remove(lst[int(col)])

print('Result matrix:')
for lst in matrix:
    print(lst)

