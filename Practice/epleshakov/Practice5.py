import os
from tempfile import mktemp
from time import sleep
from random import randint


class Man:
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)

    def solve_task(self):
        sleep(randint(3, 6))
        super().solve_task()


man1 = Man('Name')
man1.solve_task()
pup1 = Pupil('Name2')
pup1.solve_task()


class WrapStrToFile:
    def __init__(self):
        self._filepath = mktemp()

    @property
    def content(self):
        try:
            with open(self._filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return 'Файл ещё не  существует'
        except Exception as e:
            return f'Ошибка чтения файла : {e}'

    @content.setter
    def content(self, value):
        try:
            with open(self._filepath, 'w') as f:
                f.write(value)
        except Exception as e:
            print(f"Ошибка записи файла: {e}")

    @content.deleter
    def content(self):
        try:
            os.remove(self._filepath)
        except Exception as e:
            print(f"Ошибка удаления файла: {e}")


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует
print(wstf.content)