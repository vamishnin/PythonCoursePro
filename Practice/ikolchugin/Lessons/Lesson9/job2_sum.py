from multiprocessing.pool import Pool


def my_sum(*args):
    res = {}

    for arg in args:
        type_name = type(arg).__name__
        res[type_name] = res.get(type_name, type(arg)()) + arg
    return res


def main():
    p1 = ('simple', 10, [1, 2, 3, [4]], ' test ', 'string', 20,
          [5, 6, 7, [8, 9]], (30,), (40,))

    p2 = ('another', 100, [10, 20, 30, [40]], ' ', 'test ', 'string', 200,
          [50, 60, 70, [80, 90]], (300,), (400,))

    params = p1, p2

    with Pool(processes=4) as p:
        results = p.starmap(my_sum, params)

    for res in results:
        print(res)


if __name__ == '__main__':
    main()
