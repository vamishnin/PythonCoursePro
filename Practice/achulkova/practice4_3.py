arr = [0, 3, 24, 2, 3, 7]

j = 0
for i in arr:
    arr_min = min(arr[j:])
    ind_min = arr.index(arr_min, j)
    arr[j], arr[ind_min] = arr[ind_min], arr[j]
    j += 1
print(arr)
