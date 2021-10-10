import os
from tempfile import mktemp


class WrapStrToFile:
    def __init__(self):
        self._filepath = mktemp()

    @property
    def content(self):
        try:
            with open(self._filepath, 'r') as f:
                f_content = f.read()
        except FileNotFoundError:
            print("File doesn't exist")
        else:
            return f_content

    @content.setter
    def content(self, value):
        with open(self._filepath, 'w') as f:
            f.write(value)

    @content.deleter
    def content(self):
        os.remove(self._filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = "test str"
print(wstf.content)
wstf.content = "text 2"
print(wstf.content)
del wstf.content
print(wstf.content)
