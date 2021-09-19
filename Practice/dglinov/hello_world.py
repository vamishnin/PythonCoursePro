#!/bin/python
import os

print(f'Hello, {os.getlogin()}!')
print(f'You are using {os.uname().sysname}, release = {os.uname().release}!')

x = int(input('Введите любое число от 1 до 10: '))

if 0<x<11:
    print(x)
