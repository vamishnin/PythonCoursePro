while not (str := input('Enter a 5-digit number: ')).isdecimal() or len(str) != 5:
    pass

i = 1
for char in str:
    print(f'The {i}-th digit of the number is {char}')
    i += 1
