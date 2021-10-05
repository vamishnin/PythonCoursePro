def print_larger_number(a, b):
    """
    Prints maximum of two input values

    :param a: First value
    :param b: Second value
    """
    if a > b:
        print(f"larger number is {a}")
    elif a < b:
        print(f"larger number is {b}")
    else:
        print(f"a == b == {a}")

def return_larger_number(a, b):
    """
    Return maximum of values val1 and val2.

    :param a: First value
    :param b: Second value
    :return: maximum of a and b
    """
    if a > b:
        return a
    else:
        return b

print_larger_number(3, 5)
print_larger_number(3, 1)
print_larger_number(3, 3)

larger_n = return_larger_number(3,5)
print(larger_n)

