import multiprocessing as mp


def my_add(*args):
    sum = args[0]
    for i in args[1:]:
        if isinstance(i, type(args[0])):
            sum += i
    print(f"{sum=}")


if __name__ == "__main__":
    procs = []
    for i in ((1, 2, 3, 4, 5, 6, 7),
              ('1', '2', '3', '4', '5', '6', '7'),
              ([1], [2, 1], [3, 2], [4, 3])):
        procs.append(mp.Process(target=my_add, args=i))
    for i in procs:
        i.start()
    for i in procs:
        i.join()
