"""
Написать и вызвать функцию, принимающую два числа и возвращающую большее из двух.
"""
def return_max(a,b):
    if a < b: 
        return b
    else: 
        return a

print(return_max(400,2000))