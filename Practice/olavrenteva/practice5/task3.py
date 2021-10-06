import os
from tempfile import mktemp


class WrapStrToFile:
    def __init__(self):
        self.filepath = mktemp()

    @property
    def content(self):
        try:
            f = open(self.filepath, 'r')
        except FileNotFoundError:
            print("File doesn't exist")
        else:
            f_content = f.read()
            f.close()
            return f_content

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
wstf.content = "test str"
print(wstf.content)
wstf.content = "text 2"
print(wstf.content)
del wstf.content
print(wstf.content)
