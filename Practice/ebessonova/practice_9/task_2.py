import multiprocessing


def add_args(*args):
    if type(args[0]) == int:
        sum = 0
    elif type(args[0]) == str:
        sum = ''
    elif type(args[0]) == list:
        sum = list()
    for arg in args:
        sum += arg
    print(sum)


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=add_args, args=(1, 2, 3))
    t2 = multiprocessing.Process(target=add_args, args=([1, 2, 3], [5, 6, 7, 8]))
    t3 = multiprocessing.Process(target=add_args, args=('1', '2', '3'))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
