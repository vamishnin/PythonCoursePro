arr = [0, 3, 24, 2, 3, 7]

for j in arr:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)
