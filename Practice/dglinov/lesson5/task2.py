'''
Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep библиотеки time и randint библиотеки random).
'''

from task1 import Man
from time import sleep
from random import randint

class Pupil(Man):

    def solve_task(self):
        sleep(randint(3,6))
        print("I`m not ready yet")

p = Pupil('Petr')

print(p.name)
p.solve_task()