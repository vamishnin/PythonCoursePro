#Написать класс Man, который принимает имя в конструкторе.
#Имеет метод solve_task, который просто выводит "I'm not ready yet".

#Написать класс Pupil, у которого переопределен метод solve_task.
#На этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep библиотеки time и randint библиотеки random).

import time
import random


class Man:
    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print("I'm not ready yet")

class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")