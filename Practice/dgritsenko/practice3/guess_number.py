import random

while not((low := input("Введите нижнюю границу: ")).isdigit()):
    print("Введите число")

while not((high := input("Введите верхнюю границу: ")).isdigit()):
    print("Введите число")

magic_number = random.randint(int(low), int(high))
guess_try = str(int(low) - 1)
while int(guess_try) != magic_number:
    while not((guess_try := input("Попробуйте угадать число: ")).isdigit()):
        print("Введите число")

    if int(guess_try) > magic_number:
        print("Чуть меньше")
    elif int(guess_try) < magic_number:
        print("Чуть больше")

print('Верно!')