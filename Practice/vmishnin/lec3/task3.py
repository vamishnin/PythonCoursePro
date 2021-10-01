"""
Реализовать приложение, загадывающее целое число из заданного пользователем диапазона и предлагающее пользователю
это число угадать. Отгадывание числа должно быть реализовано в цикле: пока пользователь не угадает,
или не введет нечисловой символ, продолжать опрос.
Если пользователь вводит неправильное число, вывести подсказку: больше оно или меньше загаданного.
"""

import random


try:
    start = int(input("Enter start of the range: "))
    end = int(input("Enter end of the range: "))
except ValueError:
    print("Wrong range. Exiting.")
    exit(1)

number = random.randint(start, end+1)
print("Random number was generated!")

while True:
    try:
        x = int(input("Guess it: "))
    except ValueError:
        print("Not integer value. Exiting.")
        break
    if x == number:
        print(f'Grats! The number was {number}')
        break
    elif x > number:
        print("Too high!")
    elif x < number:
        print("Too low!")
