import itertools

my_list = [1, 2, 7, 2, 3, 0, 1, 1, 3, 2, 2, 5, 6, 2, 7, 0, 12, 3, 4]

sorted_list = sorted(my_list)
my_list_group_by_len = sorted((tuple(x) for _, x in itertools.groupby(sorted_list, lambda x: x)),
                              key=lambda t: (len(t), t[0]))
print(my_list_group_by_len)

res = [x[0] for x in my_list_group_by_len]
print(res)
