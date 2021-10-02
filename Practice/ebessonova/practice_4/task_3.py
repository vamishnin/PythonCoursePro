arr = [0, 3, 24, 2, 3, 7, 4, 8, 7, 15, 12]

print(f'Basic array {arr}')

counter = 0
while counter != len(arr):
    counter_in = counter + 1
    while counter_in != len(arr):
        if arr[counter_in] < arr[counter]:
            buff = arr[counter]
            arr[counter] = arr[counter_in]
            arr[counter_in] = buff
        counter_in += 1
    counter += 1

print(f'Sorted array {arr}')

