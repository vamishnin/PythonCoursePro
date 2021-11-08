# По заданному списку создать новый список, который содержит уникальные элементы изначального списка,
# расположенные в порядке возрастания количества вхождений этих элементов в изначальный список.
l1 = [3, 1, 2, 3, 3, 2, 4, 2, 3, 1]
l2 = ['odin', 'dva', 'tri', 'tri', 'dva', 'dva', 'chetyre', 'chetyre', 'dva', 'dva']


def unique_list_sort(values_list):
    unique = sorted(values_list, key=lambda x: values_list.count(x), reverse=True)
    unique_list = []
    for values in unique:
        if values not in unique_list:
            unique_list.append(values)
    return unique_list


print(unique_list_sort(l1))
print(unique_list_sort(l2))
