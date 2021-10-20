# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
import time


class TimeManager:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        ex_time = time.time() - self._start
        print(f'Execution:  {ex_time} sec')


with TimeManager():
    for i in range(0, 10001):
        sqr = i ** 0.5
        print(f'sqr({i}) = {sqr}')


