# Два потока запрашивают и выводят координаты точки на плоскости
from threading import Thread, RLock
import time


class Base:
    x = 0
    y = 0


busy = False

def print_fun(my_lock):
    i = 0
    global busy
    while i < 2:
        if not busy:
            busy = True
            Base.x = input("2x: ")
            Base.y = input("2y: ")
            print(f'Thread 2: Base.x = {Base.x}, Base.y = {Base.y}')
            busy = False
        i += 1
        #time.sleep(1)


if __name__ == '__main__':
    lock = RLock()
    t = Thread(target=print_fun, args=(lock,))
    t.start()
    i = 0
    while i < 2:
        if not busy:
            busy = True
            Base.x = input("1x: ")
            Base.y = input("1y: ")
            print(f'Thread 1: Base.x = {Base.x}, Base.y = {Base.y}')
            busy = False
        i += 1
        #time.sleep(1)
    t.join()
    