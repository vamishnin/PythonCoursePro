while 1:
    a = input('Input 5-digit number ')
    if not a.isdecimal() or len(a) != 5:
        print('Try again')
    else:
        break

num = 1
for i in a:
    print(f'{num} digit is {i}')
    num += 1

