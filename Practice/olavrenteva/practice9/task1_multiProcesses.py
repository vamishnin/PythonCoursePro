# выполняется в среднем за 0.2сек, что в 2 раза медленнее task1_multiThreads.py - неожиданный результат,
# видимо на создание процессов тратится несопоставимо больше ресурсов, чем получаемая выгода от параллельного
# запуска

import math
import time
import multiprocessing


def find_primes(end, start=3):
    res = []
    for num in range(start, end):
        if num > 1 and all(num % i for i in range(2, int(math.sqrt(num)) + 1)):
            res.append(num)
    print(res)


if __name__ == '__main__':
    start_time = time.perf_counter()
    processes = []
    for params in ((10000,), (20000, 10001), (30000, 20001)):
        p = multiprocessing.Process(target=find_primes, args=params)
        p.start()
        processes.append(p)

    for each in processes:
        each.join()

    end_time = time.perf_counter()
    print(f'Execution time is {end_time - start_time}')


