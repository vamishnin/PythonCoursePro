#! /bin/python
"""
Написать и вызвать функцию, принимающую два числа и выводящую на экран большее из двух. 
"""
def print_max(a,b):
    if a < b: 
        print(f'{b} is greater than {a}');
    else: 
        print(f'{a} is greater than {b}')

print_max(10,20)
"""
Написать и вызвать функцию, принимающую два числа и возвращающую большее из двух.
"""
def return_max(a,b):
    if a < b: 
        return b
    else: 
        return a

print(return_max(400,2000))

"""
Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.
"""
class Tank:
    def __init__(self, armor, speed):
        self.armor = armor
        self.speed = speed

    def print_stats(self):
        print(f"Armor: {self.armor}\tSpeed: {self.speed}")

heavy_tank = Tank(40, 10)
light_tank = Tank(10, 40)

heavy_tank.print_stats()
light_tank.print_stats()

