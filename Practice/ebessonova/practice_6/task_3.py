import time


class TimeCounter:

    def __enter__(self):
        self.__start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Execution time: {time.time() - self.__start} sec')


def fun():
    time.sleep(3)


with TimeCounter():
    fun()
