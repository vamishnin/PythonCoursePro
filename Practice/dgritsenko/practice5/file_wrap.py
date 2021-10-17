from os import remove
from tempfile import mktemp


class WrapStrToFIle:

    def __init__(self):
        self.path_to_file = mktemp()

    @property
    def content(self):
        try:
            with open(self.path_to_file, "r") as f:
                return f.read()
        except IOError:
            return f"File does not exist! ({self.path_to_file})"

    @content.setter
    def content(self, new_content):
        try:
            with open(self.path_to_file, "w") as f:
                f.write(new_content)
        except OSError:
            print(f"Can not write to file {self.path_to_file}!")

    @content.deleter
    def content(self):
        remove(self.path_to_file)


wrapper = WrapStrToFIle()
print(wrapper.content)
wrapper.content = 'test str'
print(wrapper.content)
wrapper.content = 'text 2'
print(wrapper.content)
del wrapper.content
