import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler:  # название класса с большой буквы

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []  # отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generate_name() + '.mp3'
            self.map[hashname] = mp3
            os.rename((path + '/' + mp3), path + '/' + hashname)  # скобки
            f = open(output, 'r')  # отступ
            f.write(str(self.map))  # отступ

    def restore(self, dirname, restore_path):
        with open(dirname, '+') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])  # лишняя скобка
        os.remove(restore_path)

    @staticmethod
    def generate_name(seed=time()):  # имя функции без больших букв
        return hashlib.md5(str(seed)).hexdigest()


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


def main():  # две пустые строки перед main
    args = parse_arguments()
    shuffler = Shuffler()  # экземпляр с маленькой буквы, класс с большой, далее исправлено аналогично
    if args.subcommand == 'rename':
        if args.output:
            shuffler.rename(args.dirname, 'restore.info')
        else:
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
