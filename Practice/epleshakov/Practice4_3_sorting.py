def sort_list(lst):
    i = 0
    while i < len(lst):
        n = i
        nxt = i + 1
        while nxt < len(lst):
            if lst[nxt] < lst[n]:
                n = nxt
            nxt += 1
        lst[i], lst[n] = lst[n], lst[i]
        i += 1


arr = [0, 3, 24, 2, 3, 7]
sort_list(arr)
print(arr)


