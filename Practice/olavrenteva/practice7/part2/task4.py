import os.path
import platform
import sys
import time


class TTLSec:
    FILE_TTL = 60
    DIR_TTL = 120


def cleaner(*args):
    dirpath = args[1]
    if os.path.exists(dirpath):
        while True:
            for path, subdirs, files in os.walk(dirpath, topdown=False):
                for file in files:
                    file_path = os.path.join(path, file)
                    time_cr = os.stat(file_path).st_birthtime if platform.system() == 'Darwin' \
                        else os.stat(file_path).st_birthtime
                    cur_t = time.time()
                    if (cur_t - time_cr) > TTLSec.FILE_TTL:
                        print(f'File {file_path} is too old, removing it')
                        os.remove(file_path)

                for subdir in subdirs:
                    subdir_path = os.path.join(path, subdir)
                    time_cr = os.stat(subdir_path).st_birthtime if platform.system() == 'Darwin' \
                        else os.stat(subdir_path).st_birthtime
                    cur_t = time.time()
                    if not os.listdir(subdir_path) and (cur_t - time_cr) > TTLSec.DIR_TTL:
                        print(f'Directory {subdir_path} is too old, removing it')
                        os.rmdir(subdir_path)

    else:
        raise ValueError(f"{dirpath} folder doesn't exist")


def create_test_data(*args):
    dirpath = args[1]

    open(os.path.join(dirpath, 'testfile_l1_1'), 'w').close()

    os.makedirs(os.path.join(dirpath, 'testdir_l1_1'))
    time.sleep(10)
    os.makedirs(os.path.join(dirpath, 'testdir_l1_1', 'testdir_l2_1_1'))
    time.sleep(10)
    os.makedirs(os.path.join(dirpath, 'testdir_l1_1', 'testdir_l2_1_2'))
    time.sleep(10)
    os.makedirs(os.path.join(dirpath, 'testdir_l1_1', 'testdir_l2_1_3'))
    time.sleep(10)
    open(os.path.join(dirpath, 'testdir_l1_1', 'testfile_l2_1_1'), 'w').close()

    os.makedirs(os.path.join(dirpath, 'testdir_l1_2'))
    os.makedirs(os.path.join(dirpath, 'testdir_l1_2', 'testdir_l2_2_1'))
    os.makedirs(os.path.join(dirpath, 'testdir_l1_2', 'testdir_l2_2_2'))
    os.makedirs(os.path.join(dirpath, 'testdir_l1_2', 'testdir_l2_2_3'))
    time.sleep(90)
    open(os.path.join(dirpath, 'testdir_l1_2', 'testfile_l2_2_1'), 'w').close()


if __name__ == '__main__':
    #create_test_data(*sys.argv)
    cleaner(*sys.argv)
