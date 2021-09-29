from random import randint


def if_user_plays():
    """
    The functions makes sure user wants to play and stops the app if user doesn't want to continue.
    :return: None
    """
    readiness = ['n', 'y', 'no', 'yes']
    while (ready := input("Are you ready? (Y/N) ")).lower() not in readiness:
        continue

    if ready.lower() == 'n' or ready.lower() == 'no':
        exit()


def if_integer(string_to_check):
    """
    The function checks if string is integer (positive or negative).
    :param string_to_check:
    :return: True or False
    """
    if (string_to_check.isdecimal() or string_to_check.startswith('-') and string_to_check[1:].isdecimal()) and \
            float(string_to_check).is_integer():
        return True
    return False


print("Let's play. You give integer interval, I think of a number and you guess it!")
if_user_plays()

while not if_integer(first_number := input("Please enter the first number of the interval: ")):
    print("Only integers are accepted")

while not if_integer(second_number := input("Please enter the second number of the interval: ")) \
        or int(second_number) <= int(first_number):
    print("Only integers are accepted and the second number must be greater than the first ")

secret_number = randint(int(first_number), int(second_number))

while if_integer(guess_number := input("Try to guess the number: ")) and int(guess_number) != secret_number:
    if int(guess_number) < secret_number:
        print(f"Secret number is greater than {guess_number}")
    else:
        print(f"Secret number is less than {guess_number}")

if not if_integer(guess_number):
    print(f"You have lost, but don't worry, just try again!")
else:
    print(f"You have won! It really was {guess_number}")
