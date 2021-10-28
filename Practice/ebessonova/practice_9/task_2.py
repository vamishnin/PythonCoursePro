import multiprocessing


def add_args(*args):
    if type(args[0]) == int:
        sum = 0
    elif type(args[0]) == str:
        sum = ''
    elif type(args[0]) == list:
        sum = list()
    type_arg = type(args[0])
    wrong_type = False
    for arg in args:
        if type(arg) == type_arg:
            sum += arg
        else:
            wrong_type = True
            break
        type_arg = type(arg)
    if not wrong_type:
        print(f'process: {multiprocessing.current_process().name}, result: {sum}')
    else:
        print(f'process: {multiprocessing.current_process().name}, result: Wrong args')


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=add_args, args=(1, 2, 3))
    t2 = multiprocessing.Process(target=add_args, args=([1, 2, 3], [1, 2, 3, 4, 5]))
    t3 = multiprocessing.Process(target=add_args, args=('1', '2', '3'))
    t4 = multiprocessing.Process(target=add_args, args=('1', '2', '3', 4))
    t5 = multiprocessing.Process(target=add_args, args=([1, 2, 3], 'asdf'))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
