import os
from tempfile import mktemp


class WrapStrToFile:
    # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища
    def __init__(self):
        self._filepath = mktemp()

    # попытка чтения из файла, в случае успеха возвращаем содержимое
    # в случае неудачи возвращаем 'File doesn't exist'
    @property
    def content(self):
        try:
            with open(self._filepath, 'r') as fp:
                return fp.read()
        except FileNotFoundError:
            a = 'File does not exist!'
            return a


    @content.setter
    def content(self, value):
        with open(self._filepath, 'w') as fp:
            fp.write(value)

    @content.deleter
    def content(self):
        os.remove(self._filepath)


wstf = WrapStrToFile()
print(wstf.content)

wstf.content = 'test str'
print(wstf.content)

wstf.content = 'text 2'
print(wstf.content)

del wstf.content
print(wstf.content)

