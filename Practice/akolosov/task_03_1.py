number = ""
while (a := input('Input a digit or the word "stop": ')).lower() != 'stop':
    if a.isdecimal() and len(a) == 1:
        number += a
    else:
        print('Incorrect input. Try again.')
else:
    print(f'The number is {int(number)}')