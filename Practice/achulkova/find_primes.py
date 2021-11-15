import time
import threading
import multiprocessing
import math


def find_primes(end, start=3):
    primes = []
    for num in range(start-1, end+1):
        prime = True
        for i in range(2, math.isqrt(num)+1):
            if num % i == 0:
                prime = False
                break
        if prime and num != 2:
            primes.append(num)
    return primes


if __name__ == '__main__':
    start = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print(f'function time: {time.perf_counter() - start: .2f} sec.')

    start = time.perf_counter()
    t1 = threading.Thread(target=find_primes, args=(10000,))
    t2 = threading.Thread(target=find_primes, args=(20000, 10001))
    t3 = threading.Thread(target=find_primes, args=(30000, 20001))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print(f'function time using threads: {time.perf_counter() - start: .2f} sec.')

    start = time.perf_counter()
    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    print(f'function time using processes: {time.perf_counter() - start: .2f} sec.')

    #Если не выполнить start для потоков, будет exception 'RuntimeError'.
    #Если не выполнить join для потоков,то главный поток завершится, не дождавшись
    #завершения дочерних потоков.
    # Если не выполнить start для процессов, будет exception 'AssertionError'.
    # Если не выполнить join для процессов,то главный поток завершится, не дождавшись
    # завершения дочерних потоков.
    #Быстрее всего выполняется вызов функции, медленнее всего происходит многопроцессное
    #выполнение функции.