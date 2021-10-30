# выполняется в среднем за 0.1сек, что чуть медленнее task1_multiThreads.py - вычисления также происходят
# последовательно, но в случае с потоками тратятся дополнительные ресурсы на их создание

import math
import time
import threading


def find_primes(end, start=3):
    res = []
    for num in range(start, end):
        if num > 1 and all(num % i for i in range(2, int(math.sqrt(num)) + 1)):
            res.append(num)
    print(res)


if __name__ == '__main__':
    start_time = time.perf_counter()
    threads = []
    for params in ((10000,), (20000, 10001), (30000, 20001)):
        t = threading.Thread(target=find_primes, args=params)
        t.start()
        threads.append(t)

    for each in threads:
        each.join()

    end_time = time.perf_counter()
    print(f'Execution time is {end_time - start_time}')


