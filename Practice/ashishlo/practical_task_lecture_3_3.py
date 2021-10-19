# 3. Реализовать приложение, загадывающее целое число из заданного пользователем диапазона и предлагающее
# пользователю это число угадать. Отгадывание числа должно быть реализовано в цикле: пока пользователь не угадает,
# или не введет нечисловой символ, продолжать опрос. Если пользователь вводит неправильное число, вывести подсказку:
# больше оно или меньше загаданного.

from random import randrange

n1 = int(input("enter first number of range: "))
n2 = int(input("enter second number of range: "))
if n2 < n1:
    n1, n2 = n2, n1
n_to_guess = randrange(n1, n2)
try_to_guess = None

while n_to_guess != try_to_guess:
    try_to_guess = int(input("Guess the number from the range: "))
    if try_to_guess == n_to_guess:
        print('SUCCESS!')
        break
    elif try_to_guess < n_to_guess:
        print("number less then the guess, try again")
    elif try_to_guess > n_to_guess:
        print("number greater then the guess, try again")



