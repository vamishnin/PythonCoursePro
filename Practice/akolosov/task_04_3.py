arr = [0, 3, 24, 2, 3, 7]

for i in range(len(arr)-1):
    min = arr[i]
    min_i = i
    for j in range(i+1,len(arr)):
        if arr[j] < min:
            min = arr[j]
            min_i = j

    arr[i], arr[min_i] = arr[min_i], arr[i]

print(f'{arr=}')