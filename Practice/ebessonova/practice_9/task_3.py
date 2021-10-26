import threading


class MyThread(threading.Thread):
    def __init__(self, a, b, c):
        threading.Thread.__init__(self)
        self.__a = a
        self.__b = b
        self.__c = c

    def run(self):
        print(f'Thread name: {threading.current_thread().name}, Args: {self.__a}, {self.__b}, {self.__c}')
        pass


if __name__ == '__main__':
    t1 = MyThread(1, 2, 3)
    t2 = MyThread(4, 5, 6)
    t3 = MyThread(10, 20, 30)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

