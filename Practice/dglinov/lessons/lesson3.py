#! /bin/python

"""
Реализовать цикл, формирующий число из вводимых пользователем символов, 
пока не будет введено слово “stop” (или “Stop”, или “STOP”).
Если пользователь ввел не числовой символ, вывести предупреждение и запросить новый символ.
"""
buf=''
while (x := input().lower()) != "stop":
    if x.isdecimal():
        buf += x
        print(buf)
    else:
        print("Вы должны ввести число!")
    

"""
Написать и вызвать функцию, проверяющую, что слово является палиндромом (примеры: “Топот”, “Довод”).
"""
data = {
    'довод',
    'топот',
    'питон',
    1999994,
    'ДоВОД',
    '     ',
}

def check_pali(a):
    if isinstance(a, str) and not a.isspace():
        x = a.lower()
        if x == x[::-1]:
            print(f"'{a}' is a palindrome")
        else: 
            print(f"'{a}' is not a palindrome")
    else:
        print("Bad input!")

for w in data:
    check_pali(w)
        
"""
Реализовать приложение, загадывающее целое число из заданного пользователем диапазона
и предлагающее пользователю это число угадать. Отгадывание числа должно быть реализовано 
в цикле: пока пользователь не угадает, или не введет нечисловой символ, продолжать опрос. 
Если пользователь вводит неправильное число, вывести подсказку: больше оно или меньше загаданного. 
"""

from random import randint

a, b = input("Enter 2 numbers > 0 to set the range.\nFormat - 'NUM1','NUM2': ").split(",")

if not a.isdecimal() or not b.isdecimal():
    print("Something wrong! You need to type two numbers "
          "> 0 to set the range according to the format!!!")    
    exit(1)

r_min = min(int(a), int(b))
r_max = max(int(a), int(b))
secret = randint(r_min, r_max)

attempts = 0
while (x:=input(f"Try to guess my number in range {r_min} to {r_max}:\t")).isdecimal():
    attempts += 1
    if int(x) < secret: 
        print(f"My number is bigger than {x}!")
    elif int(x) > secret: 
        print(f"My number is smaller than {x}!")
    else: 
        print(f'Congrats!!! The secret number is {secret}!\nYou take {attempts} attempts.')
        break
