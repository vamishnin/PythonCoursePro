import subprocess
from subprocess import Popen, PIPE

"""
С помощью библиотеки subprocess прочитать содержимое произвольного файла 
с использованием утилиты cat в Linux или type в Windows 
(имя файла должно передаваться как параметр в вашу функцию).
"""

def catfile(filepath):
    proc = Popen(['TYPE', filepath], stdout=PIPE, stderr=PIPE, shell=True)
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1].decode('cp866'))
    print(res[0].decode('cp866'))


tutu = catfile('myfile.txt')
