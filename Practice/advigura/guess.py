import random
myrange = int(input('Enter range '))
# number = 23 
number = random.randint(0, myrange)

while True:
    guess = input('Введите целое число : ')
    if not guess.isdigit(): 
        break
    else:
        guess = int(guess)
    if guess == number: 
        print('Поздравляю, вы угадали!') 
        break
    elif guess < number: 
        print('Нет, загаданное число немного больше этого.') 
    else: 
        print('Нет, загаданное число немного меньше этого.') 
    # чтобы попасть в else, guess должно быть больше, чем number 
print('Завершено') 
