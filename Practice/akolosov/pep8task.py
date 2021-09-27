import sys
import os
import hashlib
import ast
import argparse
from time import * # Вместо * надо указать конкретные функции


class shuffler: # неправильное имя класса

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = [] # неправильный отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s: # выше нужно разделить пустой строкой
            hashname = self.generateName() + '.mp3' # неправильное имя функции
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r') # неправильный отступ
          f.write(str(self.map)) # неправильный отступ

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: # неправильный отступ
            self.map = ast.literal_eval(f.read()) # неправильный отступ
          mp3s = [] # неправильный отступ
          # нужна разделительная пустая строка
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3': # неправильный отступ
                    mp3s.append({root, file})
        for path, hashname in mp3s: # выше нужно разделить пустой строкой
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
            # последняя скобка выше лишняя
        os.remove(restore_path)
                
     def generateName(self, seed=time()):
          # выше неправильный отступ, неправильное имя функции
          return hashlib.md5(str(seed)).hexdigest() # неправильный отступ


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    # выше неправильная длина строки. часть аргументов нужно перенести
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main(): # выше нужно добавить пустую строку
    args = parse_arguments()
    Shuffler = shuffler() # неправильное имя класса
    if args.subcommand == 'rename':
          if args.output: # неправильный отступ
                Shuffler.rename(args.dirname, 'restore.info')
                # выше неправильный отступ
          else: # неправильный отступ
                Shuffler.rename(args.dirname, args.output)
                # выше неправильный отступ
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
