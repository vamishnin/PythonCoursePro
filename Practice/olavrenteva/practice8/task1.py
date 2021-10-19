def generate_sorted_list(init_list):
    temp_list = [(el, init_list.count(el)) for el in set(init_list)]
    temp_list.sort(key=lambda x: (x[1], x[0]))
    return [i[0] for i in temp_list]


lst = [0, 0, 10, 1, 15, 20, 10, 10, 0, -5, 1, 20, 100, 0]
print(generate_sorted_list(lst))
