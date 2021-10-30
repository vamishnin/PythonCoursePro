import os
import sys
import time


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: /bin/python3 {sys.argv[0]} path_to_dir")
        exit(1)
    
    try:
        os.chdir(sys.argv[1])
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        exit(1)

    while True:
        it = os.scandir()
        empty = True
        lst = []
        while True:
            # walk throught the dir and enter into each a subdir
            try:
                item = next(it)
            except StopIteration:
                it.close()
                if len(lst) == 0:
                    break
                else:
                    # return from a subdir
                    # 'empty_up' is a state of the current dir
                    # 'empty' is a state of the subdir
                    it, item, empty_up = lst.pop()                    
                    if empty and (time.time() - item.stat().st_mtime) > 120:
                        os.rmdir(item.path)
                        empty = empty_up
                    else:
                        empty = False # current dir contains a subdir
                    # now 'empty' is a state of the current dir
                    continue

            if item.is_file():
                if (time.time() - item.stat().st_mtime) > 60:
                    os.remove(item.path)
                else:
                    empty = False # the current dir contains a file
            elif item.is_dir():
                # save the current state
                lst.append([it, item, empty])
                # enter into a subdir
                it = os.scandir(item.path)
                empty = True

        time.sleep(10)

