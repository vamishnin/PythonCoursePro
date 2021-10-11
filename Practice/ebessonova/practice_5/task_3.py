import os
import tempfile


class WrapStrToFile:

    def __init__(self):
        self.filepath = tempfile.mktemp(dir='./')

    @property
    def content(self):
        try:
            f = open(self.filepath, 'r')
            f_text = f.read()
            f.close()
            return f_text
        except FileNotFoundError:
            return 'File doesn\'t exist'

    @content.setter
    def content(self, value):
        f = open(self.filepath, 'w')
        f.write(value)
        f.close()

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
