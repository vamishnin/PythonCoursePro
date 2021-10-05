#! /bin/python
"""
Написать и вызвать функцию, принимающую два числа и выводящую на экран большее из двух. 
"""
def print_max(a,b):
    if a < b: 
        print(f'{b} is greater than {a}')
    else: 
        print(f'{a} is greater than {b}')

print_max(10,20)