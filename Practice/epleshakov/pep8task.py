import sys
import os
import hashlib
import ast
import argparse
from time import *  # Импортируется всё из time, не проще простой импорт использовать? import time


class Shuffler:  # Название класса не с большой буквы

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []  # Два избыточных пробела до объявления переменной mp3s.
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename((path + '/' + mp3), path + '/' + hashname)  # Не хватает скобки перед path
            # и лишняя после hashname
        f = open(output, 'r')  # Два избыточных пробела
        f.write(str(self.map))  # Два избыточных пробела

    def restore(self, dirname, restore_path):
        with open(dirname, '+') as f:  # Два избыточных пробела, переменная filename не определена.
            # Возможно имелось ввиду dirname?
            self.map = ast.literal_eval(f.read())  # Лишняя скобка в конце
        mp3s = []  # Два избыточных пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':  # Не хватает пробела
                    mp3s.append({root, file})  # Не хватает трех пробелов
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])  # Лишняя скобка в конце
        os.remove(restore_path)

# Пробелы вместо одной пустой строки
    def generateName(self, seed=time()):  # Лишний пробел, Имя функции написано в формате CamelCase.
        # Желательно должно разделяться нижним подчеркиванием с маленьких букв т.н. snake_case
        return hashlib.md5(str(seed)).hexdigest()  # Два избыточных пробела


# Одна пустая строка вместо двух - отделение от методов класса Shuffler
def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


# Одна пустая строка вместо двух - отделение от методов класса Shuffler
def main():
    args = parse_arguments()
    shuffler = Shuffler()  # Описание переменной и класса перепутаны, Название переменной в верхнем регистре,
    # а класса в нижнем
    if args.subcommand == 'rename':
        if args.output:  # лишние два пробела
            shuffler.rename(args.dirname, 'restore.info')  # Название переменной в верхнем регистре, лишние два пробела
        else:  # лишние два пробела
            shuffler.rename(args.dirname, args.output)  # Название переменной в верхнем регистре, лишние два пробела
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)  # Название переменной в верхнем регистре
    else:
        sys.exit()


main()
