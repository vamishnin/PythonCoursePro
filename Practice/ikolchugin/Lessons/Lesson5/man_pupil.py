from time import sleep
from random import randint


class Man:
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    def solve_task(self):
        print('I''m ready')


class Pupil(Man):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)

    def solve_task(self):
        sleep(randint(3, 6))
        super(Pupil, self).solve_task()


man1 = Man('Ivan')
man1.solve_task()

man2 = Pupil('Petr')
man2.solve_task()
