from task_1 import Man
import time
import random


class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print('I\'m not ready yet')


pup = Pupil('Petr')
print(pup.name)
pup.solve_task()
