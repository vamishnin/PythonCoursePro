# вариант 1 - условие в шапке
num = ''
a = ''
while a.lower() != 'stop':
    a = input('введите цифру или "stop": ')
    if a == 'stop':    # если ввели 'stop', то дальнейшие действия в теле цикла не производим - возвр. на проверку
        continue
    if a.isdigit():
        num = num + a
    else:
        print(f'"{a}" не является цифрой')
print(f'ваше число: {num}')


# вариант 2 - с break
x = ''
while True:
    y = input('введите цифру или "stop": ')
    if y.lower() == 'stop':
        break
    if y.isdigit():
        x = x + y
    else:
        print(f'"{y}" не является цифрой')

print(f'ваше число: {x}')




