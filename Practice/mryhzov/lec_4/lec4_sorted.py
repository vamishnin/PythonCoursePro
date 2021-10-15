# Реализовать алгоритм сортировки выбором.
lst1 = [0, 3, 24, 2, 3, 7]


def sort_list(lst):
    i = 0
    while i < len(lst):
        n = i
        next_n = i + 1
        while next_n < len(lst):
            if lst[next_n] < lst[n]:
                n = next_n
            next_n += 1
        lst[i], lst[n] = lst[n], lst[i]
        i += 1
    return lst


print(sort_list(lst1))

# lst1 = [8, 3, 24, 2, 0, 5, 7]
# lst2 = []
# i = 0
# len1 = len(lst1)
# while i <= (len1-1):
#     min_num = min(lst1)
#     ind_min = lst1.index(min_num)
#     lst2.append(lst1.pop(ind_min))
#     i += 1
# print(lst2)
