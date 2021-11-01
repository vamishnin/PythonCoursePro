import sys
import os
import hashlib
import ast
import argparse
from time import time


class Shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-4:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generate_name() + '.mp3'
            self.map[hashname] = mp3
            os.rename(os.path.join(path, mp3), os.path.join(path, hashname))
        with open(output, 'w') as f:
            f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(restore_path, 'r') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-4:] == '.mp3':
                    mp3s.append([root, file])
        for path, hashname in mp3s:
            os.rename(os.path.join(path, hashname), os.path.join(path, self.map[hashname]))
        os.remove(restore_path)
    
    @staticmethod            
    def generate_name():
            return hashlib.md5(str(time()).encode()).hexdigest()


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

def main():
    args = parse_arguments()
    shuffler = Shuffler()
    if args.subcommand == 'rename':
        if not args.output:
            shuffler.rename(args.dirname, 'restore.info')
        else:
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
