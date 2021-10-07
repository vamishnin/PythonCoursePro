# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить
# слово Fizz, а вместо чисел, кратных пяти — слово Buzz.
# Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz.

list1 = list(range(1, 101))
for i in list1:
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
