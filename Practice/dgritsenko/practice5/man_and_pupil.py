import random
from time import sleep


class Man:

    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print('Im not ready yet!')


class Pupil(Man):

    __pause_low_bound_sec = 3
    __pause_high_bound_sec = 6

    def solve_task(self):
        sleep(random.randint(self.__pause_low_bound_sec, self.__pause_high_bound_sec))
        print('Im not ready yet!')


man = Man('Ivan')
pupil = Pupil('Petr')
man.solve_task()
pupil.solve_task()
