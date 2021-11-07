from subprocess import Popen, PIPE

cmd = 'TYPE'
filename = 'lec7_1.py'
p = Popen([cmd, filename], stdout=PIPE, shell=True)    # Popen - сохраняет вывод консоли в пайп stdout=PIPE
result = p.communicate()[0]    # извлечение данных из пайпа. нужное значение - 1й элемент кортежа
print(result.decode())

