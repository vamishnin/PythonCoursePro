def print_max_of(val1, val2):
    """
    Prints maximum of values val1 an val2.

    :param val1: First value
    :param val2: Second value
    """
    if val1 > val2:
        print_val = val1
    else:
        print_val = val2
    print(f'1. Function print_max_of({val1}, {val2}) prints {print_val}')


def max_of(val1, val2):
    """
    Return maximum of values val1 and val2.

    :param val1: First value
    :param val2: Second value
    :return: maximum of val1 and val2
    """
    if val1 > val2:
        max_val = val1
    else:
        max_val = val2
    return max_val


val1 = input('Input first number: ')
val2 = input('Input second number: ')

print_max_of(val1, val2)
print(f'2. Function max_of({val1}, {val2}) returns {max_of(val1, val2)}')

