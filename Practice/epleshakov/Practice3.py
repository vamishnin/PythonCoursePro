'''
Практика №3
Q1 - input_to_sum() сложение чисел. input_to_conn() - конкатенация чисел
Q2 - is_palindrome(str) Проверка слова или фразы на полиндромность
'''


def input_to_sum():
    temp = float()
    while True:
        x = input('Enter number or "stop": ')
        if x.replace('-', '').replace('.', '').isdigit():
            temp += float(x)
        elif x.lower() == 'stop':
            print('Stopped')
            break
        else:
            print(f'Wrong value: {x}')
    if temp % 1 == 0:  # Если число целое, то приведение к int() чтобы убрать .0 в выводе
        print(f'Sum of latest numbers: {int(temp)}')
    else:
        print(f'Sum of latest numbers: {temp}')


def input_to_conn():
    temp = ''
    while True:
        x = input('Enter number or "stop": ')
        if x.replace('-', '').replace('.', '').isdigit():
            temp += x
        elif x.lower() == 'stop':
            print('Stopped')
            break
        else:
            print(f'Wrong value: {x}')
    print(f'Concatenated numbers: {temp}')

#input_to_sum()
input_to_conn()

def is_palindrome(a):
    temp_A = a.replace(' ', '').lower()
    temp_B = temp_A[::-1]
    return temp_A == temp_B


f = 'Топот'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')

f = 'Кит на море романтик'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')

f = 'Кот на море романтик'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')
