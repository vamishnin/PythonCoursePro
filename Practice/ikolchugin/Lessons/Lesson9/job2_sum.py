from multiprocessing.pool import ThreadPool


def my_sum(*args):
    res = {}
    for arg in args:
        type_name = type(arg).__name__
        try:
            res[type_name] += arg
        except KeyError:
            res[type_name] = arg
    return res


def main():
    p1 = ('simple', 10, [1, 2, 3, [4]], ' test ', 'string', 20,
          [5, 6, 7, [8, 9]], (30,), (40,))

    p2 = ('another', 100, [10, 20, 30, [40]], ' ', 'test ', 'string', 200,
          [50, 60, 70, [80, 90]], (300,), (400,))

    params = p1, p2

    pool = ThreadPool(processes=4)
    async_result = []

    for p in params:
        async_result.append(pool.apply_async(my_sum, p))

    for res in async_result:
        print(res.get())


if __name__ == '__main__':
    main()
