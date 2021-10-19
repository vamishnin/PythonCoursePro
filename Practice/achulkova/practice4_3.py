arr = [0, 3, 24, 2, 3, 7]

for i in range(len(arr)-1):
    min_el = arr[i]
    min_ind = i
    for j in range(i+1, len(arr)):
        if arr[j] < min_el:
            min_el = arr[j]
            min_ind = j

    arr[i], arr[min_ind] = arr[min_ind], arr[i]

print(f'{arr=}')
