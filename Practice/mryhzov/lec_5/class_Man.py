from random import randint
from time import sleep

#  Unable to get repr for <class '__main__.Man'>
class Man:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Hello, i am {self.name}'

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