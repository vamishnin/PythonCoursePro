'''
Практика №3
Q1 - input_to_sum() сложение чисел
Q2 - is_palindrome(str) Проверка слова или фразы на полиндромность
'''
import re

def input_to_sum():
    temp = float()
    while True:
            x = input('Enter number or "stop": ')
            temp_x = re.split("\.|-", x)
            temp_x = ''.join(temp_x)
            if temp_x.isdigit():
                temp += float(x)
                if temp % 1 == 0:
                    print(f'Sum of latest numbers: {int(temp)}')
                else:
                    print(f'Sum of latest numbers: {temp}')
            elif x.lower() == 'stop':
                print('Stopped')
                break
            else:
                print(f'Wrong value: {x}')


input_to_sum()


def is_palindrome(a):
    temp_A = a.split()
    temp_A = ''.join(temp_A)
    temp_B = a[::-1].split()
    temp_B = ''.join(temp_B)
    if temp_A.lower() == temp_B.lower():
        return True
    return False


f = 'Топот'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')

f = 'Кит на море романтик'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')
