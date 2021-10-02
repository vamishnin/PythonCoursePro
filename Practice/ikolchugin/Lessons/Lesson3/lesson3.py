x = ''
res = ''

while True:
    x = input("Input digit or 'stop' to stop input: ")

    if x.isdigit():
        res += x
    elif x.upper() != 'STOP':
        print(f'Ожидается число')
    else:
        break

print(res)