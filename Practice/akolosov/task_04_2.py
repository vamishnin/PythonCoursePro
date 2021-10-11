while not (s := input('Enter a 5-digit number: ')).isdecimal() or len(s) != 5:
    pass

i = 1
for char in s:
    print(f'The {i}-th digit of the number is {char}')
    i += 1
