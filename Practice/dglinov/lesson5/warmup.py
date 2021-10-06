
def my_enum(lst):
    i = 0
    tmp = []
    for el in lst:
        tmp.append((i, el))
        i += 1
    return tmp

def mymax(lst):
    max_v = 0
    for i, v in my_enum(lst):
        if max_v < v:
            max_v = v
    return max_v

data = [1,2,3,4,5]

print(mymax(data))
print(my_enum(data))

