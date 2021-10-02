def chars_to_num():
    b = ''
    while 1:
        a = input('Write number ')
        if a.lower() == 'stop':
            break
        if a.isdecimal():
            b += a
        else:
            print('Its not a number')
    return b

print(chars_to_num())