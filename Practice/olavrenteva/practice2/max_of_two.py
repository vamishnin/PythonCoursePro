def find_max_of_two(val1, val2):
    return val1 if val1 >= val2 else val2


def print_max_of_two(val1, val2):
    max_value = find_max_of_two(val1, val2)
    print(max_value)


x = 5
y = -1
max_x_y = find_max_of_two(x, y)
print(f'{max_x_y=}')
print_max_of_two(y, x)



