import random

#Task1
s = int()
while True:
    x = input('Enter number: ')
    if x.isdigit():
        s += int(x)
    elif x == 'stop' or x == 'Stop' or x == 'STOP':
        break
    else:
        print('WRONG: enter number!')
print(f'Result: {s}')


#Task2
def palindrom():
    lst = input("Enter word: ")

    if lst == lst[::-1]:
        print("This is a palindrom.")
    else:
        print("This is not a palindrome.")
palindrom()


#Task3
start = int(input("Enter number: "))
end = int(input("Enter number: "))
num = random.randint(start, end)

def guess_number(a):
    while True:
        x = input("Enter number: ")

        if not x.isdigit():
            print("WRONG! Enter number.")
        elif int(x) > a:
            print("Number less.")
        elif int(x) < a:
            print("Number more.")
        elif int(x) == a:
            print("Correct number.")
            break

guess_number(num)


