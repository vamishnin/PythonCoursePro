def print_max(a: int, b: int):
    if a > b:
        print(f"Max value: {a}")
    else:
        print(f"Max value: {b}")


# How many ways can I call the function?
print_max(1, 11)

print_max(b=2, a=55)

my_list=[3, 99]
print_max(*my_list)

my_dict={'b': 4, 'a': 22}
print_max(**my_dict)

my_dict={'b': 77}
print_max(**my_dict, a=5)
