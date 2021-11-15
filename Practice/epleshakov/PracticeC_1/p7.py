# Написать функцию copyfile: функция принимает два аргумента – имена файлов source и destination, открывает source,
#  читает его, открывает destination, пишет в него.
# Если source не найден или destination уже существует, то выбрасываются соответствующие исключения.
# Нужно проверить выполнение функции как для правильных аргументов, так и для приводящих к исключениям.
import os.path


def copyfile(source, destination):
    try:
        with open(source, 'r') as src_file:
            src = src_file.read()
            if os.path.exists(destination):
                raise FileExistsError
            else:
                with open(destination, 'x') as dst_file:
                    dst_file.write(src)
    except FileNotFoundError:
        print(f'Файл {source} не найден')
    except FileExistsError:
        print(f'Файл {destination} уже существует')

copyfile('Teory.txt', 't1.txt')