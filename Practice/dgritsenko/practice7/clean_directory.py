import sys
from os import path, mkdir
from os import walk
from os import listdir

FOLDER_TTL_SEC, FILE_TTL_SEC = 10, 5

def clean_directory(*args):
    folder_path = args[0]

    while True:
        f = []
        for (dirpath, dirnames, filenames) in walk(folder_path):
            print(dirpath, dirnames)

        # for files in listdir(folder_path):
        #     print(files)
        break


def create_test_dir(path_to_file):
    if not path.exists(path_to_file):
        mkdir(path_to_file)
    mkdir(path.join(path_to_file, 'dir1'))
    mkdir(path.join(path_to_file, 'dir2'))
    with open(path.join(path_to_file, 'dir1', 'text.txt'), 'w') as f1:
        f1.write('Hello!')
    with open(path.join(path_to_file, 'text1.txt'), 'w') as f1:
        f1.write('Goodbye!')


if __name__ == '__main__':
    if len(*sys.argv) != 1 or not isinstance(sys.argv[0], str):
        print("Bad arguments!")
        exit

    if not path.exists(sys.argv[0]):
        print(f"Folder {sys.argv[0]} does not exist")
        exit

    path_to_file = 'test'

    create_test_dir(path_to_file)
    clean_directory(path_to_file)



