def remove_number(lst: list, number: int):
    '''
    Remove all rows contained the number
    '''
    to_remove = set()
    for sublst in lst:
        for i in range(len(sublst)):
            if sublst[i] == number:
                to_remove.add(i)
    
    to_remove = tuple(sorted(to_remove, reverse=True))
    
    for sublst in lst:
        for index in to_remove:
            if index < len(sublst): # protection from bad data (not rectangle)
                del sublst[index]
            else:
                continue

    return lst


if __name__ == "__main__":
    arr = [
            [1,  2,  3,  4,  5,  6,  7,  8,  9],
            [11, 12, 13, 2,  15, 16, 2,  18, 19],
            [21, 2,  23, 24, 25, 26, 27, 28, 29]
    ]

    print(remove_number(arr, 2))

    arr = [
           [5, 5, 5, 5, 5, 5, 5, 5, 3],
           [5, 5, 5, 5, 3, 5, 5, 5, 5],
           [5, 5, 5, 5, 5, 5, 5, 5, 5]
    ]

    print(remove_number(arr, 3))