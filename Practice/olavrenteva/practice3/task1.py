result = ''

while (entered_symbol := input("Please enter the next digit or STOP to finish: ")).lower() != 'stop':
    if entered_symbol.isdigit():
        result += entered_symbol
    else:
        print(f'{entered_symbol} is not a digit, only digits are acceptable')

print(f'You have entered {int(result)}')
