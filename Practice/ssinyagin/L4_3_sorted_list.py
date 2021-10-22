def mysorted(my_list):
    z = len(my_list)
    k = 0
    new_list = []
    while k < z:
        j = 0
        x = 0
        for i in my_list:
            if my_list[j] <= my_list[x]:
                x = j
            j += 1
        new_list.append(my_list.pop(x))
        k += 1
    return new_list

st_list = [0, 3, 24, 2, 3, 7]
print(f'Исходный список: {st_list}')
res_list = mysorted(st_list)
print(f'Сортированный список: {res_list}')