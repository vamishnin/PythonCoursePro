from subprocess import Popen, PIPE


def console_read_file(filename):
    proc = Popen(['cat', filename], stdout=PIPE, stderr=PIPE)
    res = proc.communicate()

    if proc.returncode:
        return res[1].decode('cp866')
    return res[0].decode('cp866')


result = console_read_file('./task_5.py')
print(f'result executing cat command : \n{result}')