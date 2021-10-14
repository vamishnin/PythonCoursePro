
def my_enum(lst):
    i = 0
    tmp = []
    for el in lst:
        tmp.append((i, el))
        i += 1
    return tmp

def mymax(lst):
    max_v = float('-inf')
    for i, v in my_enum(lst):
        if max_v < v:
            max_v = v
    return max_v

data = [1,2,3,4,5,-100]

data_negative = [-1,-2,-3,-4,-5,-100]


if __name__ == '__main__':
    print(mymax(data))
    print(mymax(data_negative))

    print(my_enum(data))
    print(my_enum(data_negative))

