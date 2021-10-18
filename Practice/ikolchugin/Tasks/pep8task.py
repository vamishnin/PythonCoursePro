import sys
import os
import hashlib
import ast
import argparse
from time import time  # мне нужен только time


class Shuffler:  # названия классов в формате ClassName

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []  # неправильный отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
                # Рекомендуется проверять начало или конец  строки
                # при помощи startswith и endswith
                if file.endswith('.mp3'):
                    mp3s.append([root, file])
        # добавил пустую строку, чтобы отделить обход структуры ФС
        # от обработки результата обхода
        for path, mp3 in mp3s:
            # Название функции в нижнем регистре с подчёркиванием
            hashname = self.generate_name() + '.mp3'

            self.map[hashname] = mp3
            # разделитель пути в Windows другой
            # используем независимую от ОС склейку пути и имени файла
            # перенос строки, длина больше 76
            os.rename(os.path.join(path, mp3),
                      os.path.join(path, hashname))
        # добавил пустую строку,
        # чтобы отделить обработку результата обхода от записи файла
        # исправлены отступы, изменён режим открытия файла для записи.
        f = open(output, 'w')
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
        # отступы исправлены
        # filename не определён, имя файла передано в  restore_path
        # режим '+' без r|w|a не существует,
        # для чтения содержимого файла нужно как минимум 'r'
        with open(restore_path, 'r') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []

        for root, directories, files in os.walk(dirname):
            for file in files:
                if file.endswith('.mp3'):  # аналогично стр. 19
                    mp3s.append([root, file])  # список это [], а не {}
        # добавил пустую строку, чтобы отделить обход структуры ФС
        # от обработки результата обхода
        for path, hashname in mp3s:
            os.rename(os.path.join(path, hashname),
                      os.path.join(path, self.map[hashname]))  # см стр.29-30
        os.remove(restore_path)

    # при первом вызове будет задано значение seed = time(),
    # которое не будет меняться при последующих вызовах функции,
    # всегда  будет возвращаться одинаковое значение, это неправильно
    @staticmethod
    def generate_name(seed=None):
        t_seed = time() if seed is None else seed
        # неправильный отступ
        # параметром md5  является бинарное значение, а не строка.
        return hashlib.md5(str(t_seed).encode('utf-8')).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand',
                                       help='subcommand help')
    rename_parser = subparsers.add_parser('rename',
                                          help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output',
                        help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore',
                                           help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


# Добавлена пустая строка, чтобы было 2 пустые строки между функциями
def main():
    args = parse_arguments()
    # название переменной в нижний регистр, название класса -по стр. 10
    shuffler = Shuffler()
    if args.subcommand == 'rename':
        if args.output:  # исправлены отступы
            # неверное использование условия.
            # Если есть args.output, то и следует использовать его.
            shuffler.rename(args.dirname, args.output)
        else:
            shuffler.rename(args.dirname, 'restore.info')
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
