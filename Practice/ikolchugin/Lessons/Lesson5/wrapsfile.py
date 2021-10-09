import os
from tempfile import mktemp


class WrapStrToFile:
    def __init__(self):
        self._filepath = mktemp()

    @property
    def content(self):
        try:
            with open(self._filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "File doesn't exist"
        except Exception as e:
            return "File read error: {}".format(e)

    @content.setter
    def content(self, value):
        try:
            with open(self._filepath, 'w') as f:
                f.write(value)
        except Exception as e:
            print("File write error: {}".format(e))

    @content.deleter
    def content(self):
        try:
            os.remove(self._filepath)
        except Exception as e:
            print("File delete error: {}".format(e))

wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует
print(wstf.content)
