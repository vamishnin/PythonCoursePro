def generate_sorted_list(init_list):
    temp_dict = {}
    for el in init_list:
        temp_dict[el] = temp_dict.get(el, 0) + 1

    return [key for key, value in sorted(temp_dict.items(), key=lambda x: (x[1], x[0]))]


lst = [0, 0, 10, 1, 15, 20, 10, 10, 0, -5, 1, 20, 100, 0]
print(generate_sorted_list(lst))
