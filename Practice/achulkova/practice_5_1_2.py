from time import sleep
from random import randint


class Man:
    def __init__(self, name: str):
        self.name = name
        print(f"{name} says: ")

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name: str):
        self.name = name
        print(f"{name} says: ")

    def solve_task(self):
        sleep(randint(3, 6))
        print("I'm not ready yet")


man1 = Man('Ivan')
man1.solve_task()
man2 = Pupil('Petr')
man2.solve_task()

