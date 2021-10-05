'''
Практика №3
Q1 - input_to_sum() сложение чисел. Два варианта. С регулярными выражениями (import re) в комментариях и с replace()
Q2 - is_palindrome(str) Проверка слова или фразы на полиндромность
'''
#import re

def input_to_sum():
    temp = float()
    while True:
        x = input('Enter number or "stop": ')
        #temp_x = re.split("\.|-", x)
        #temp_x = ''.join(temp_x)
        temp_x = x.replace('-', '').replace('.', '')
        print(temp_x)
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
    temp_A = a.replace(' ', '')
    temp_B = a[::-1].replace(' ', '')
    if temp_A.lower() == temp_B.lower():
        return True
    return False


f = 'Топот'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')

f = 'Кит на море романтик'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')

f = 'Кот на море романтик'

print(f'{f=}, is Polyndrom?: {is_palindrome(f)}')
