from random import randint
from time import sleep


class Man:
    def __init__(self, _name):
        self._name = _name

    def __repr__(self):
        return f'Hello, i am {self._name}'

    def solve_task(self):
        print("I'm not ready yet")


man1 = Man('Alex')
print(man1)
man1.solve_task()


class Pupil(Man):

    def solve_task(self):
        rand_time = randint(3, 6)
        sleep(rand_time)
        print("I think slowly")


pup1 = Pupil('Boris')
print(pup1)
pup1.solve_task()