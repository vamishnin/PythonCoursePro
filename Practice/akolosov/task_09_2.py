import threading
import multiprocessing as mp


def my_add(*args):
    sum = args[0]
    for i in args[1:]:
        if isinstance(i, type(args[0])):
            sum += i
    print(f"{sum=}")


if __name__ == "__main__":
    print("Threads:")
    threads = []
    threads.append(threading.Thread(target=my_add, args=(1, 2, 3, 4, 5, 6, 7)))
    threads[0].start()
    threads.append(threading.Thread(target=my_add, args=('1', '2', '3', '4', '5', '6', '7')))
    threads[1].start()
    threads.append(threading.Thread(target=my_add, args=([1], [2, 1], [3, 2], [4, 3])))
    threads[2].start()
    for i in threads:
        i.join()

    print("Processes:")
    procs = []
    procs.append(mp.Process(target=my_add, args=(1, 2, 3, 4, 5, 6, 7)))
    procs[0].start()
    procs.append(mp.Process(target=my_add, args=('1', '2', '3', '4', '5', '6', '7')))
    procs[1].start()
    procs.append(mp.Process(target=my_add, args=([1], [2, 1], [3, 2], [4, 3])))
    procs[2].start()
    for i in procs:
        i.join()
