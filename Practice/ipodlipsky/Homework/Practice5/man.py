import time
import random
import tempfile

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")

class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))

class WrapStrToFile:

    def __init__(self, filepath):
        self.filepath = tempfile.mktemp()

    # def mktemp(self):
    #     self.name = tempfile.mktemp()



