import random


def input_num(a: str):
    '''
    Input a correct number
    '''
    while not (string := input(f'Input the {a} number of the range: ')).isdecimal():
        pass

    return int(string)


if __name__ == "__main__":
    begin = input_num('first')
    end = input_num('last')
    if begin > end:
        begin, end = end, begin
    guessing_number = random.randint(begin, end)
    print('The guessing number has been created. Try to guess.')

    while (string := input(f'Input a suggested number: ')).isdecimal():
        suggested_number = int(string)
        if suggested_number == guessing_number:
            print('Congratulation!! The right number!!')
            break
        elif suggested_number > guessing_number:
            print('Your number is more then the guessing number')
        else:
            print('Your number is less then the guessing number')
    else:
        print('You will guess next time')
