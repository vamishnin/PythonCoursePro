def max(a, b):
    if a > b:
        print(f'max {a}')
    elif b > a:
        print(f'max {b}')
    else:
        print('equal')

max(6, 5)


def max_r(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

res = max_r(6, 6)
print(res)