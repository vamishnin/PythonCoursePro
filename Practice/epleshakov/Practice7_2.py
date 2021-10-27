# С помощью библиотеки subprocess прочитать содержимое произвольного файла с использованием утилиты cat в Linux
# или type в Windows (имя файла должно передаваться как параметр в вашу функцию).
from subprocess import Popen, PIPE


def type_file(filename):
    proc = Popen(['cmd', '/c', 'type', filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1].decode('cp866'))
        #print(res[1])
    print('result:', res[0].decode('utf-8'))
    return res[0].decode('utf-8')


type_file('P7_0.txt')
