# def sort_choice(array, start_index=0):
#     if len(array[start_index:]) <= 1:
#         return
#
#     index_min = start_index
#     for i in range(start_index+1, len(array)):
#         if array[i] < array[index_min]:
#             index_min = i
#     if index_min != start_index:
#         array[start_index], array[index_min] = array[index_min], array[start_index]
#
#     sort_choice(array, start_index+1)

def sort_choice(array):
    if len(array) <= 1:
        return

    for i in range(len(array) - 1):
        index_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_min]:
                index_min = j
        if index_min != i:
            array[i], array[index_min] = array[index_min], array[i]


array = [2, 1, 2, 4, 3, -5, 1, 10, 0, -20, -0.5]
sort_choice(array)
print(array)
