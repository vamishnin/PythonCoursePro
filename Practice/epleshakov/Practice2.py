def print_max(a, b):
    print(max(a, b))


def is_max(a, b):
    return max(a, b)


def print_max2(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print('Numbers is equal')


def is_max2(a, b):
    if a < b:
        return b
    elif a > b:
        return a
    return None


first = input('Inter first number: ')
second = input('Inter second number: ')


print_max(first, second)
print_max2(first, second)

print('MAX number is: ' + is_max(first, second))
print('MAX number is: ' + is_max2(first, second))
