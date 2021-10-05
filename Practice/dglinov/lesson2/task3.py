#! /bin/python
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

