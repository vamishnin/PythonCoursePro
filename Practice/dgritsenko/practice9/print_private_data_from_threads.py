from threading import Thread
from threading import current_thread


class CustomThread(Thread):
    def __init__(self, data):
        super().__init__()
        self.__data = data

    def run(self):
        print(f"Thread name: {current_thread().name}, thread data: {self.__data}\n")


if __name__ == '__main__':
    t1 = CustomThread('data')
    t2 = CustomThread(['d', 'a', 't', 'a'])
    t3 = CustomThread(123456789)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
