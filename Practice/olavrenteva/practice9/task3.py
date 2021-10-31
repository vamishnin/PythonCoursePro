import threading
import time


def some_func(thread_storage):
    thread_storage.time = time.time()
    print(f'{threading.current_thread().name}, {thread_storage.time} \n')


if __name__ == '__main__':
    private_data = threading.local()

    t1 = threading.Thread(target=some_func, args=(private_data,))
    t1.start()
    t2 = threading.Thread(target=some_func, args=(private_data,))
    t2.start()
    t1.join()
    t2.join()
