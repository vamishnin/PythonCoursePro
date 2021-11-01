import multiprocessing


def sum_objects(*args):
    if len(args) == 0:
        raise TypeError('sum_objects requires at least 1 argument')

    if not all(isinstance(args[i], type(args[0])) for i in range(1, len(args))):
        raise ValueError('all arguments should be objects of the same type')

    res = args[0]
    for i in range(1, len(args)):
        res += args[i]

    print(res)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sum_objects, args=(1, 2, 3, 4, 5))
    p1.start()
    p2 = multiprocessing.Process(target=sum_objects, args=('a', 'b', 'c'))
    p2.start()
    p3 = multiprocessing.Process(target=sum_objects, args=([1, 2], ['a', 'b']))
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('all processes are finished')