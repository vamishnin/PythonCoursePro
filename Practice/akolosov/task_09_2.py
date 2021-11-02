import threading
import multiprocessing as mp
import time


def my_add(*args):
    sum = args[0]
    for i in args[1:]:
        if isinstance(i, type(args[0])):
            sum += i
    print(f"{sum=}")


if __name__ == "__main__":
    print("Threads:")
    start = time.perf_counter()
    threads = []
    for i in ((1, 2, 3, 4, 5, 6, 7),
              ('1', '2', '3', '4', '5', '6', '7'),
              ([1], [2, 1], [3, 2], [4, 3])):
        threads.append(threading.Thread(target=my_add, args=i))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print(f'Threads total time: {time.perf_counter() - start}')

    print("Processes:")
    start = time.perf_counter()
    procs = []
    for i in ((1, 2, 3, 4, 5, 6, 7),
              ('1', '2', '3', '4', '5', '6', '7'),
              ([1], [2, 1], [3, 2], [4, 3])):
        procs.append(mp.Process(target=my_add, args=i))
    for i in procs:
        i.start()
    for i in procs:
        i.join()
    print(f'Processes total time: {time.perf_counter() - start}')
    # Threads is faster in ~10-15 times than processes
    # because the 'cost' of creation subproccess much bigger than the function execution
