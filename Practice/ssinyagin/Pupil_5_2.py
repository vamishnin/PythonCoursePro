import time
import random
from Man_5_1 import Man


class Pupil(Man):

    def solve_task(self):
        t = random.randint(3, 6)
        time.sleep(t)
        print(t)
        return super().solve_task()


chel = Pupil('Geg')
chel.solve_task()
