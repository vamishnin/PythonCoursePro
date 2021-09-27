import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler: #наименование класса в формате CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = [] #неправильный отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3, path + '/' + hashname) #лишние скобки
        f = open(output, 'r') #неправильный отступ
        f.write(str(self.map)) #неправильный отступ

    def restore(self, dirname, restore_path):
        with open(restore_path, '+') as f: #неправильный отступ, в функцию open передавался не существующий аргумент
            self.map = ast.literal_eval(f.read())
            mp3s = [] #неправильный отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]) #лишние скобки
            os.remove(restore_path) #неправильный отступ

    def generateName(self, seed=time()): #неправильный отступ
        return hashlib.md5(str(seed)).hexdigest() #неправильный отступ


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


def main(): # добавлена 2-я пустая строка между функциями
    args = parse_arguments()
    shuffler = Shuffler() #наименование класса - с большой буквы, переменной - с маленькой
    if args.subcommand == 'rename':
        if args.output: #неправильный отступ
            shuffler.rename(args.dirname, 'restore.info')
        else: #неправильный отступ
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
