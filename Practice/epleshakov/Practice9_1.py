import threading
import multiprocessing
import time


# Декоратор для подсчета времени выполнения функций
def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print(f"Функция '{func.__name__}' с аргументами {args} выполнилась за {time.perf_counter() - t:.3f} секунды")
        return res
    return wrapper

# Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного
# числа start (по умолчанию 3) до заданного числа end.

# Пробовал воспользоваться декоратором для подсчета времени функции,
# но multiprocessing отказывается с ним работать
# @benchmark
def find_primes(end: int, start=3):
    ls = []
    while start <= end:
        j = 2
        while j <= start:
            if start % j == 0:
                if j == start:
                    ls.append(j)
                break
            j += 1
        start += 1
    print(ls)
    # return ls

# Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.Thread.
# Что будет, если 'забыть' выполнить start или join для потоков?
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process.
# Что будет, если 'забыть' выполнить start или join для процессов?
#  - Если не указать метод join, то вызвавший их поток (сама программа в данном случае) не будут
# ожидать выполнения этого потока и продолжит свою работу. Т.е. выведется счетчик времени раньше чем
# потоки закончат свою работу.
#  - Если не запустить метод start выскочит исключение "cannot join thread before it is started". Т.к
# нечего ожидать
#  - Для процессов аналогично

if __name__ == '__main__':
    print('Without threads')
    start_time = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print(f'Without threads done! Time: {time.perf_counter() - start_time:.2f} sec.')

    print('With threads')
    start_time = time.perf_counter()
    threads = []
    threads.append(threading.Thread(target=find_primes, args=(10000,)))
    threads.append(threading.Thread(target=find_primes, args=(20000, 10001)))
    threads.append(threading.Thread(target=find_primes, args=(30000, 20001)))
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()
    print(f'Threads done! Time: {time.perf_counter() - start_time:.2f} sec.')

    print('With threads 2') # Для проверки влияния места запуска метода start()
    start_time = time.perf_counter()
    threads = []
    thr = threading.Thread(target=find_primes, args=(10000,))
    threads.append(thr)
    thr.start()
    thr2 = threading.Thread(target=find_primes, args=(20000, 10001))
    threads.append(thr2)
    thr2.start()
    thr3 = threading.Thread(target=find_primes, args=(30000, 20001))
    threads.append(thr3)
    thr3.start()
    for thr in threads:
        thr.join()
    print(f'Threads 2 done! Time: {time.perf_counter() - start_time:.2f} sec.')

    print('With Processes')
    start_time = time.perf_counter()
    procs = []
    proc1 = multiprocessing.Process(target=find_primes, args=(10000,))
    procs.append(proc1)
    proc1.start()
    proc2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    procs.append(proc2)
    proc2.start()
    proc3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    procs.append(proc3)
    proc3.start()
    for proc in procs:
        proc.join()

    print(f'Processes done! Time: {time.perf_counter() - start_time:.2f} sec.')


# Замерить время исполнения каждого варианта и сравнить результаты.
#  - Судя по результатам - С процессами получилось быстрее чуть менее чем наполовину.
# c потоками особой разницы нет, место вызова метода start() тоже не оказывает влияния.
# Without threads done! Time: 5.78 sec.
# Threads done! Time: 5.65 sec.
# Threads 2 done! Time: 5.67 sec.
# Processes done! Time: 3.54 sec.