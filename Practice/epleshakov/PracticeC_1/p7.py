# Написать функцию copyfile: функция принимает два аргумента – имена файлов source и destination, открывает source,
#  читает его, открывает destination, пишет в него.
# Если source не найден или destination уже существует, то выбрасываются соответствующие исключения.
# Нужно проверить выполнение функции как для правильных аргументов, так и для приводящих к исключениям.
import os.path


def copyfile(source, destination):
    with open(source, 'r') as src_file:
        with open(destination, 'x') as dst_file:
            dst_file.writelines(src_file)

copyfile('Teory.txt', 't1.txt')