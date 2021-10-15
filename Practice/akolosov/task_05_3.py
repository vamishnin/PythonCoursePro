import os
import tempfile


class WrapStrToFIle:

    def __init__(self):
        self.__filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self.__filepath, "r") as f:
                return f.read()
        except IOError:
            return "File doesn't exist"

    @content.setter
    def content(self, value):
        with open(self.__filepath, "w") as f:
            if isinstance(value, str):
                f.write(value)
            else:
                f.write(str(value))
        return None

    @content.deleter
    def content(self):
        os.remove(self.__filepath)
        return None


if __name__ == "__main__":
    wstf = WrapStrToFIle()
    print(wstf.content)
    wstf.content = "It is only warm-up"
    print(wstf.content)
    del wstf.content
    wstf.content = 'It', 'is', 'a', 'super', 'puper', 'program'
    print(wstf.content)
    wstf.content = 1625425
    print(wstf.content)
    del wstf.content
