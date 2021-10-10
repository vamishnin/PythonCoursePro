arr = [0, 3, 24, 2, 3, 7]


def find_min_idx_since_pos(in_arr, pos):
    if not len(arr) > pos >= 0:
        return

    minimum = float('inf')
    idx_min = pos
    for p in range(pos, len(arr)):
        if arr[p] < minimum:
            minimum = in_arr[p]
            idx_min = p

    print(idx_min)
    return idx_min


def selection_sort(arr):
    pos = 0
    while pos != len(arr) - 1:
        idx_min = find_min_idx_since_pos(arr, pos)
        arr[pos], arr[idx_min] = arr[idx_min], arr[pos]
        pos += 1


selection_sort(arr)

print(arr)