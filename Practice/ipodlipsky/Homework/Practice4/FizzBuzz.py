# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
# а вместо чисел, кратных пяти — слово Buzz.
# Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz.

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 != 0 and i % 15 != 0:
#         #print(f'{i} кратно 3-ём')
#         print(f'Fizz')
#     elif i % 5 == 0 and i % 3 != 0 and i % 15 != 0:
#         print(f'Bazz')
#     elif i % 15 == 0:
#         print(f'FizzBuzz')
#     else:
#         print(i)

i = 1
#while i < 101: или
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    #i += 1