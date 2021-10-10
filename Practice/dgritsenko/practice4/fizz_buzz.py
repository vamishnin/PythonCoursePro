import random

NUMBERS_CNT = 10
LOW_NUMBER_BOUND = 1
HIGH_NUMBER_BOUND = 100

i = 0
while i < NUMBERS_CNT:
    magic_num = random.randint(LOW_NUMBER_BOUND, HIGH_NUMBER_BOUND)

    if magic_num % 15 == 0:
        print('FizzBuzz')
    elif magic_num % 3 == 0:
        print('Fizz')
    elif magic_num % 5 == 0:
        print('Buzz')
    else:
        print(magic_num)

    i += 1

