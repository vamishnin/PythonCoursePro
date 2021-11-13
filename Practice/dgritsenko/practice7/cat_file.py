from os import path
from subprocess import Popen, PIPE


def read_file_with_cat(path_to_file):
    if not path.exists(path_to_file):
        return ""

    proc = Popen(['cat', path_to_file], stdout=PIPE, stderr=PIPE)
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1])
        return ""
    return res[0]

print(read_file_with_cat("file_to_read.txt"))