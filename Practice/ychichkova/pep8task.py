import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler: #название класса начинается в верхнем регистре 

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []# неправильный отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            # лишние скобки после hashname
            os.rename(path + '/' + mp3), path + '/' + hashname ''

        f = open(output, 'r') # неправильный отступ
        f.write(str(self.map)) # неправильный отступ

    def restore(self, dirname, restore_path):
        with open(dirname, '+') as f: # неправильный отступ
            self.map = ast.literal_eval(f.read())

        mp3s = [] # неправильный отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
        os.remove(restore_path)

    def generateName(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest()

    def parse_arguments(self): # определения методов внутри класса разделяются одной пустой строкой и неправильный отступ
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

    def main(self): # неправильный отступ и добавить ссылку на экземпляр класса
        args = self.parse_arguments() # для вызова parse_arguments() нужно добавить  self.
        shuffler = Shuffler() # переменные начинаются в нижнем регистре, классы в верхнем

        if args.subcommand == 'rename':
            if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
            else:
                Shuffler.rename(args.dirname, args.output)
        elif args.subcommand == 'restore':
            Shuffler.restore(args.dirname, args.restore_map)
        else:
            sys.exit()

    main()
