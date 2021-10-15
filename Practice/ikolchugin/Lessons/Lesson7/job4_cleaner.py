import os

import shutil
from time import sleep, time


FOLDER_TTL, FILE_TTL = 120, 60


def clean_dir(directory_name, folder_ttl=FOLDER_TTL, file_ttl=FILE_TTL):
    curr_time = time()
    print('start watch')
    for root, directories, files in os.walk(directory_name):
        for file in files:
            f_stat = os.stat(file)
            if f_stat.st_mtime_ns > curr_time + file_ttl:
                print(f'Need to delete {file=} {f_stat}')
                os.remove(file)
        for dir in directories:
            d_stat = os.stat(os.path.join(root, dir))
            if d_stat.st_mtime_ns > curr_time + folder_ttl:
                print(f'Need to delete {dir=} {d_stat}')
                shutil.rmtree(dir, ignore_errors=False)
    print('end watch\n')
    print(f'{curr_time=}')


dir_to_clean = os.path.join(os.path.dirname(__file__),'test_dir')
while True:
    try:
        clean_dir(dir_to_clean)
        sleep(1)
    except KeyboardInterrupt:
        print('Interrupted by user')
        break
