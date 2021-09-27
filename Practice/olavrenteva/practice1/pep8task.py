import sys
import os
import hashlib
import ast
import argparse
from time import *


#class shuffler:
# renamed to conform CapWord style:
class Shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        #  mp3s = []
        # removed extra indents:
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                #if file[-3:] == '.mp3':
                # '.' is -4th symbol:
                if file[-4:] == '.mp3':
                    mp3s.append([root, file])

        # added empty line between blocks:
        for path, mp3 in mp3s:
            #hashname = self.generateName() + '.mp3'
            # corrected function name:
            hashname = self.generate_name() + '.mp3'
            self.map[hashname] = mp3
            #os.rename(path + '/' + mp3), path + '/' + hashname))
            # removed extra brackets:
            os.rename(path + '/' + mp3, path + '/' + hashname)
          #f = open(output, 'r')
          #f.write(str(self.map))

        # added empty line between blocks,
        # removed extra indents, r replaced with w to write:
        f = open(output, 'w')
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
          #with open(filename, '+') as f:
          #  self.map = ast.literal_eval(f.read())
          # mp3s = []
        # removed extra indents, undefined filename replaced with restore_path,
        # + mode doesn't exist, so it's replaced with r
        with open(restore_path, 'r') as f:
            self.map = ast.literal_eval(f.read())  # removed extra indents

        # added empty line between blocks:
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               #if file[-3:] == '.mp3':
               # '.' is -4th symbol:
                if file[-4:] == '.mp3':
                    #mp3s.append({root, file})
                    # {} is dict, but we use list here:
                    mp3s.append([root, file])

        # added empty line between blocks:
        for path, hashname in mp3s:
            #os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
            # removed extra brackets:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
        os.remove(restore_path)
                
    # def generateName(self, seed=time()):
    #      return hashlib.md5(str(seed)).hexdigest()
    # removed extra indents, func is renamed to be lowercase,
    # added encode('utf-8') as Unicode-objects must be encoded before hashing,
    # moved seed definition to the body to have different hashes for files:
    def generate_name(self):
        seed = time()
        return hashlib.md5(str(seed).encode('utf-8')).hexdigest()


# one more empty line is added before the function to have two lines after class definition:
def parse_arguments():
    parser = argparse.ArgumentParser()
    #subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    # added line break to don't exceed 79 symbols per line:
    subparsers = parser.add_subparsers(dest='subcommand',
                                       help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    #rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    # added line break to don't exceed 79 symbols per line:
    rename_parser.add_argument(
                        '-o', '--output',
                        help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


# one more empty line is added before the function to have two lines
# between high-level functions
def main():
    args = parse_arguments()
#    Shuffler = shuffler()
    # var name in lower case, class name in CapWord:
    shuffler = Shuffler()
    # if args.subcommand == 'rename':
    #       if args.output:
    #             Shuffler.rename(args.dirname, 'restore.info')
    #       else:
    #             Shuffler.rename(args.dirname, args.output)
    # removed extra indents, corrected mixed conditions for 'rename',
    # Shuffler replaced with shuffler (object name):
    if args.subcommand == 'rename':
        if args.output:
            shuffler.rename(args.dirname, args.output)
        else:
            shuffler.rename(args.dirname, 'restore.info')
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
