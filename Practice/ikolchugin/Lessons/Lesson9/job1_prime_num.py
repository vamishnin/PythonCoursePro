import threading
import multiprocessing
import time

RUN_COUNT = 3


def find_primes(end, start=3):
    t_start = time.perf_counter()
    primes = [i for i in range(3, end + 1, 2)]
    upper_bound = end ** 0.5
    for base in range(len(primes)):
        if not primes[base]:
            continue
        if primes[base] >= upper_bound:
            break
        for i in range(base + (base + 1) * primes[base], len(primes), primes[base]):
            primes[i] = None
    primes.insert(0, 2)
    res = tuple(filter(lambda x: x is not None and x >= start, primes))
    t_stop = time.perf_counter()
    print(f'find_primes {start}-{end}: {t_stop-t_start=:2.5f}ms')
    return res


def gen_params(_num=RUN_COUNT, _start=3, _step=10000):
    for _i in range(0, _num):
        if _i > 0:
            j = _i * _step
            yield j + 1, j + _step
        else:
            j = 2
            yield j + 1, _step


if __name__ == '__main__':

    print('Simple use')
    for start, end in gen_params(7):
        find_primes(end, start)
    time.sleep(0.1)

    print('Use Threads')
    threads = []
    for start, end in gen_params(7):
        thr = threading.Thread(target=find_primes, args=(end, start))
        thr.start()

    for thr in threads:
        thr.join()

    time.sleep(0.1)

    print('Use Processes')
    processes = []
    for start, end in gen_params(7):
        process = multiprocessing.Process(target=find_primes, args=(end, start))
        process.start()

    for p in processes:
        p.join()


