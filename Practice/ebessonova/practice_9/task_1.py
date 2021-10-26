from threading import Thread
import multiprocessing
import time


def calc_simple_numbers(end, start=3):
    simple_lst = list()
    for num in range(start, end):
        simple = True
        for div_num in range(2, num):
            if num % div_num == 0:
                simple = False
                break
        if simple:
            simple_lst.append(num)
    # print(simple_lst)


if __name__ == '__main__':
    time_start = time.time()
    calc_simple_numbers(10000)
    calc_simple_numbers(20000, 10001)
    calc_simple_numbers(30000, 20001)
    print(f'calculation functions time: {time.time() - time_start}')

    time_start = time.time()
    t1 = Thread(target=calc_simple_numbers, args=(10000, ))
    t2 = Thread(target=calc_simple_numbers, args=(20000, 10001))
    t3 = Thread(target=calc_simple_numbers, args=(30000, 20001))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print(f'calculation functions time with threads: {time.time() - time_start}')
    # время вычисления функции разделенной потоками совпадает со временем вычисления функций последовательно,
    # из-за работы GIL распараллеливание вычислений посредством потоков не осуществимо
    # если убрать функция start() поток не будет запущен и функция ен выполняется
    # если убрать join() не дожидаемся завершения выполнения функций в вызывающем потоке и выполняем следующие операции
    # в главном потоке, в данном случае вывод времени выполнения

    time_start = time.time()
    t1 = multiprocessing.Process(target=calc_simple_numbers, args=(10000,))
    t2 = multiprocessing.Process(target=calc_simple_numbers, args=(20000, 10001))
    t3 = multiprocessing.Process(target=calc_simple_numbers, args=(30000, 20001))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print(f'calculation functions time with processes: {time.time() - time_start}')
    # время вычисления с использованием процессов сократилось примерно в 2 раза
