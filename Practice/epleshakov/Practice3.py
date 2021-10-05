'''
Практика №3
Q1 - input_to_sum() сложение чисел.
Q2 - is_palindrome(str) Проверка слова или фразы на полиндромность
'''

def input_to_sum():
    temp = ''
    while True:
        x = input('Enter number or "stop": ')
        if x.lower() == 'stop':
            if temp % 1 == 0:  # Если число целое, то приведение к int() чтобы убрать .0 в выводе
                print(f'Sum of latest numbers: {int(temp)}')
            else:
                print(f'Sum of latest numbers: {temp}')
            break
        if x.replace('-', '').replace('.', '').isdigit():
            temp += float(x)
        else:
            print(f'Wrong value: {x}')


input_to_sum()


def is_palindrome(a):
    temp_A = a.replace(' ', '').lower()
    temp_B = temp_A[::-1]
    if temp_A == temp_B:
        return True
    return False


f = 'Топот'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')

f = 'Кит на море романтик'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')

f = 'Кот на море романтик'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')
