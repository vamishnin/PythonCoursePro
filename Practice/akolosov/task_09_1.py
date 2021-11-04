import multiprocessing as mp
import threading
import math
import time


def find_prime(end: int, start = 3):
    if ( not isinstance(end, int)) or (not isinstance(start, int)) or end < start:
        return []
    lst = []
    for num in range(start, end + 1):
        # if num has multipliers then the square of the smallest multiplier can't be more than num
        # it is enought to find the smallest multiplier
        for i in range(2, math.isqrt(num) + 1):
            if (num % i) == 0:
                break
        else:
            lst.append(num)
    return lst


if __name__ == "__main__":
    start = time.perf_counter()
    print(len(find_prime(1000000)))
    print(len(find_prime(2000000, 1000001)))
    print(len(find_prime(3000000, 2000001)))
    print(f'Total time: {time.perf_counter() - start}')
    # ~17sec

    start = time.perf_counter()
    threads = []
    for i in ((1000000,), (2000000, 1000001), (3000000, 2000001)):
        threads.append(threading.Thread(target=find_prime, args=i))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print(f'Threads total time: {time.perf_counter() - start}')
    # Without start() we get an exception 'RuntimeError' at join()
    # Without join() the main thread waits for the subthreads
    # but all commands of main thread finish before the subthreads
    # becase of that the time measure is wrong
    # ~22sec

    start = time.perf_counter()
    procs = []
    for i in ((1000000,), (2000000, 1000001), (3000000, 2000001)):
        procs.append(mp.Process(target=find_prime, args=i))
    for i in procs:
        i.start()
    for i in procs:
        i.join()
    print(f'Processes total time: {time.perf_counter() - start}')
    # Without start() we get an exception 'AssertionError' at join()
    # Without join() the main process waits for the subprocesses
    # but all commands of main process finish before the subprocess
    # becase of that the time measure is wrong
    # ~8-9sec
