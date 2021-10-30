from subprocess import Popen, PIPE

proc = Popen(['cat', 'task5.py'], stdout=PIPE)

res = proc.communicate()
print(res[0].decode('utf-8'))

