import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp(dir='./')

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print('File doesn\'t exist')

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(value)
            #f.close()

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
