# Реализовать алгоритм сортировки выбором.

lst1 = [0, 3, 24, 2, 3, 7]
lst2 = []    # Не смог корректно реализовать замену символов в первичном списке, ввел второй
i = 0
while i <= 5:
    min_num = min(lst1)
    ind_min = lst1.index(min_num)
    lst1.pop(ind_min)
    lst2.append(min_num)
    i = i + 1
print(lst2)





# lst1 = [0, 3, 24, 2, 3, 7]
# for i in lst1:
#     min_num = min(lst1)
#     ind_min = lst1.index(min_num)
#     lst1[0], lst1[ind_min] = lst1[ind_min], lst1[0]
#     print(lst1)

# lst1 = lst1[ind:]
# for i in lst1:
#     min_num = min(lst1)
#     ind = lst1.index(min_num)
#     # print(min_num)
#     # print(ind)
#     lst1.insert(0, min_num)
#     lst1.pop(ind+1)
#     print(lst1)
