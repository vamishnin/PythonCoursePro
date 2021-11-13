import sys
from multiprocessing import Process
from time import sleep
from threading import Thread

sys.path.insert(0, '../practice6')

from context_manager import TimeManager


def find_primes(end, start):
    if end < 0 or start < 0:
        return

    primes = []

    step = 1 if end > start else -1

    for n in range(start, end + step, step):
        i = 2
        is_prime = True
        while i <= n / 2:
            if n % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            primes.append(n)

    #sleep(1)
    return primes


def generate_input():
    input_step = 10000
    num_iter = 3
    for i in range(num_iter):
        yield [input_step * i + (3 if not i else 1), input_step * (i+1)]


if __name__ == '__main__':

    with TimeManager():
        for start, end in generate_input():
            find_primes(end, start)

    threads = []
    for start, end in generate_input():
        threads.append(Thread(target=find_primes, args=(end, start)))
    with TimeManager():
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    processes = []
    for start, end in generate_input():
        processes.append(Process(target=find_primes, args=(end, start)))
    with TimeManager():
        for p in processes:
            p.start()
        for p in processes:
            p.join()

