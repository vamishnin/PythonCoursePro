import random
from time import sleep


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil:
    def solve_task(self):
        sleep(random.randint(3, 6))
        print("I'm not ready yet")


man = Man("Vasya")
pupil = Pupil()
man.solve_task()
pupil.solve_task()
