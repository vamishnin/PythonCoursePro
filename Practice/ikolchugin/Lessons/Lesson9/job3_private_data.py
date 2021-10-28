import threading
import time
from random import randint

class MyThread(threading.Thread):
    def __init__(self, name=None):
        threading.Thread.__init__(self)
        if name is None:
            self.__thread_name = self.getName()
        else:
            self.__thread_name = name

    def print_private(self):
        print(f'My private data is {self.__thread_name=}, current thread_name is {self.getName()}')
        time.sleep(0.5)

    def run(self):
        self.print_private()

my_threads = []



for i in range(2):
    t = MyThread(f'myThread_{i}_{randint(13,40)}')
    t.start()
    my_threads.append(t)

for i in range(2):
    t = MyThread(f'SuperThread_{i}_{randint(45,50)}')
    t.start()
    my_threads.append(t)

for i in range(4):
    t = MyThread()
    t.start()
    my_threads.append(t)

for t in my_threads:
    t.join()