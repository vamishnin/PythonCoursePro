# выполняется в среднем за 0.08-0.1сек

import math
import time


def find_primes(end, start=3):
    res = []
    for num in range(start, end):
        if num > 1 and all(num % i for i in range(2, int(math.sqrt(num)) + 1)):
            res.append(num)
    print(res)


if __name__ == '__main__':
    start = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    end = time.perf_counter()
    print(f'Execution time is {end - start}')
