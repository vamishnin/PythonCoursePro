arr = [0, 3, 24, 2, 3, 7]
j = 0


def my_min(a, b):
    arr_min = min(a[b:])
    index_min = a.index(arr_min, b)
    return index_min


for i in arr:
    x = my_min(arr, j)
    arr[j], arr[x] = arr[x], arr[j]
    j += 1
print(arr)
