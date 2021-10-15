from datetime import datetime
from random import randint
from time import sleep


class TestManager:

    def __enter__(self):
        print('Starting code inside manager')
        self._start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        _duration = datetime.now() - self._start
        print(f'Code completed. Error info: type - {exc_type}')
        print(f'Code run duration is {_duration} ')


with TestManager():
    print(1 + 1)
    sleep(randint(1, 5))
