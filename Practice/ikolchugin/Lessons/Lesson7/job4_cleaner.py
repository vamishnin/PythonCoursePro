import os
from time import sleep, time
import argparse
from sys import exit

FOLDER_TTL, FILE_TTL = 120, 60


def clean_dir(directory_name, folder_ttl=FOLDER_TTL, file_ttl=FILE_TTL):
    print('Check directory for objects to delete')
    curr_time = time()

    for root, _, files in os.walk(directory_name):
        for _file in files:
            t_file = os.path.join(root, _file)
            f_stat = os.stat(t_file)
            if curr_time > f_stat.st_ctime + file_ttl:
                print(f'Need to delete file {t_file} {f_stat.st_ctime}')
                os.remove(t_file)

    # После удаления файла из каталога у каталога изменяется ctime.
    # Если учитывать изменение ctime каталога после удаления файла, то нужно перед удалением файлов
    # предварительно пройтись по дереву каталогов и получить ctime для каждого каталога,
    # сохранить время и название каталога в словаре  {path: ctime}, например.
    # но этот вариант, как мне кажется, необоснованно усложняет решение задачи.
    for root, directories, _ in os.walk(directory_name):
        for _dir in directories:
            t_dir = os.path.join(root, _dir)
            d_stat = os.stat(t_dir)
            if curr_time > d_stat.st_ctime + folder_ttl:
                print(f'Need to delete directory {t_dir} {d_stat.st_ctime}')
                try:
                    os.rmdir(t_dir)
                except Exception as e:
                    print(e)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Directory cleaner removes files older than 1 min '
                    'and empty directories older than 2 min.')
    parser.add_argument('-d', action="store", dest="dirname", required=True,
                        help="Directory to watch and clean")
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    try:
        while True:
            try:
                clean_dir(args.dirname)
                sleep(1)
            except KeyboardInterrupt:
                print('Interrupted by user')
                break
    except Exception as e:
        print(e)
        exit(-1)


if __name__ == '__main__':
    main()
