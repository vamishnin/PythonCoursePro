def remove_number(lst: list, number: int):
    '''
    Remove all rows contained the number
    '''
    to_remove = set()
    for sublst in lst:
        for i in range(len(sublst)):
            if sublst[i] == number:
                to_remove.add(i)
    
    for sublst in lst:
        i = 0
        for index in to_remove:
            if (index - i) < len(sublst):
                del sublst[index-i]
                i += 1
            else:
                break
    ### The second way of the second part:
    # to_remove = list(to_remove)
    # to_remove.reverse()
    # to_remove = tuple(to_remove)
    # for sublst in lst:
    #     for index in to_remove:
    #         if index < len(sublst):
    #             del sublst[index]
    #         else:
    #             continue

    return lst


arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
       [11, 12, 13, 2, 15, 16, 2, 18, 19],
       [21, 2, 23, 24, 25, 26, 27, 28, 29]]

print(remove_number(arr, 2))
