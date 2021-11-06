import time
import random

class Man:
    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print(f'{self._name}: I\'m not ready yet"')

class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print(f'{self._name}: I\'m not ready yet"')

m = Man('Ivan')
m.solve_task()

p = Pupil('Kolya')
p.solve_task()