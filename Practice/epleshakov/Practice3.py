'''
Практика №3
Q1 - input_to_num()
Q2 - is_palindrome(str)
'''
def input_to_num():
    temp = int()
    while True:
        x = input('Enter number or "stop": ')
        if x.isdigit():
            print(f'Number is: {x}')
            temp += int(x)
            print(f'Sum of latest numbers: {temp}')
        elif x.lower() == 'stop':
            print('Stopped')
            break
        else:
            print(f'Wrong value: {x}')


input_to_num()

def is_palindrome(a):
    temp_A = a.split()
    temp_A = ''.join(temp_A)
    print(temp_A)
    temp_B = a[::-1].split()
    temp_B = ''.join(temp_B)
    print(temp_B)
    if temp_A.lower() == temp_B.lower():
        return True


f = 'Топот'

print(is_palindrome(f))

f = 'Кит на море романтик'

print(is_palindrome(f))
