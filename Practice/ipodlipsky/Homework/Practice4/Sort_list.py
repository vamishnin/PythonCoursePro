arr = [3, 0, 24, 2, 3, 7]
print(arr)

def sort_list(nums):
    for i in range(len(nums)):
        min_idx = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                 min_idx = j
            else:
                 nums[i], nums[min_idx] = nums[min_idx], nums[i]

sort_list(arr)
print(arr)


