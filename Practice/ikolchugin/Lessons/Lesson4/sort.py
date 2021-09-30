arr = [0, 3, 24, 2, 3, 7]


def index_of_min(lst):
    idx_min = 0
    t_min = lst[idx_min]

    for t in range(1, len(lst)):
        if lst[t] < t_min:
            t_min = lst[t]
            idx_min = t
    return idx_min


for i in range(len(arr)):
    idx = i + index_of_min(arr[i:])
    arr[i], arr[idx] = arr[idx], arr[i]
print(arr)
