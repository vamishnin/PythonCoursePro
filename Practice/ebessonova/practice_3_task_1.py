def chars_to_num():
    b = ''
    while 1:
        try:
            a = input('Write number ')
            if a == 'stop' or a == 'Stop' or a == 'STOP':
                break
            b += str(int(a))
        except ValueError:
            print('Its not a number')
    return b

print(chars_to_num())