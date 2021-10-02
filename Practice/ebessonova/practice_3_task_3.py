import random


def guess_num(low, high):
    riddle_number = random.randrange(int(low), int(high))
    while 1:
        in_num = input(f'Guess number from interval [{low}, {high}] : ')
        if int(in_num) > riddle_number:
            print('Need lower')
        elif int(in_num) < riddle_number:
            print('Need higher')
        else:
            print('You puzzled it out')
            break


while 1:
    low = input('Input lower boundary ')
    high = input('Input upper boundary ')
    if low.isdecimal() != True or high.isdecimal() != True or int(low) >= int(high):
        print('Try again')
    else:
        break

guess_num(low, high)
