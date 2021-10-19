#Написать и вызвать функцию, принимающую два числа и выводящую на экран большее из двух.

def max_num(a: int, b: int):
    print(a) if a > b else print(b)

#Написать и вызвать функцию, принимающую два числа и возвращающую большее из двух
def more_num(a: int, b: int):
    return a if a > b else b




# Примеры вызова функции max_num
max_num(15, 10)
max_num(1.5, 1)
max_num(-15, 10)
max_num(-15, -10)

# Примеры вызова функции more_num
s = more_num(15, 10)
print(s)
s = more_num(1.5, 1)
print(s)
s = more_num(-15, 10)
print(s)
s = more_num(-15, -10)
print(s)