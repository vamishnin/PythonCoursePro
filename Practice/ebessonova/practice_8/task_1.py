def new_list(input_list):
    count_dict = dict()
    for el in input_list:
        count_dict[el] = count_dict.get(el, 0) + 1

    sorted_dict = sorted(count_dict.items(), key=lambda num: num[1])
    output_list = list()
    for elem in sorted_dict:
        output_list.append(elem[0])
    return output_list


print(new_list([1, 2, 1, 3, 1, 4, 4, 5, 4, 6, 4, 7, 4, 7, 5, 5]))

print(new_list([1, 1, 2, 4, 4, 4, 4, 4, 3, 3]))


