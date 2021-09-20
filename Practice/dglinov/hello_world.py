#!/bin/python
import os

print(f'Hello, {os.getlogin()}!')
print(f'You are using {os.uname().sysname}, release = {os.uname().release}!')

print(f'Echo: {input("Type Something: ")}\n' * 3)