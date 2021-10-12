import os
import tempfile


class WrapStrToFile:

    def __init__(self):
        self.__filepath = tempfile.mktemp(dir='./')

    @property
    def content(self):
        try:
            with open(self.__filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return 'File doesn\'t exist'

    @content.setter
    def content(self, value):
        with open(self.__filepath, 'w') as f:
            f.write(value)

    @content.deleter
    def content(self):
        os.remove(self.__filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
