# Варианты с max()
def print_max(a, b):
    print(f"(print_max)Biggest number is: {max(int(a), int(b))}")


def is_max(a, b):
    return max(int(a), int(b))


# Варианты с if
def print_max2(a, b):
    if int(a) > int(b):
        print(f"(print_max2)Biggest number is: {a})")
    elif int(a) < int(b):
        print(f"(print_max2)Biggest number is: {b}")
    else:
        print('(print_max2)Numbers is equal')


def is_max2(a, b):
    if int(a) > int(b):
        return a
    elif int(a) < int(b):
        return b
    return None


first = input('Inter first number: ')
second = input('Inter second number: ')

print_max(first, second)
print_max2(first, second)

print(f'(is_max)MAX number is: {is_max(first, second)}')
print(f'(is_max2)MAX number is: {is_max2(first, second)}')
