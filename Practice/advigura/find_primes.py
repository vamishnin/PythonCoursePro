import threading
import multiprocessing
import time


def find_primes(end, start = 3):
    primes = []
    for i in range(start, end):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(primes)
    return primes


    

if __name__ == '__main__':  
    
    
    start = time.perf_counter() 
    print(f'{find_primes(10000, 3)}')
    print(f'{find_primes(20000, 10001)}')
    print(f'{find_primes(30000, 20001)}')
    print(f'{time.perf_counter() - start:.2f} sec.')
    
    start = time.perf_counter() 
    threads = []
    t1 = threading.Thread(target=find_primes, args=(10000, 3))
    t1.start()
    threads.append(t1)
    
    t2 = threading.Thread(target=find_primes, args=(20000, 10001))
    t2.start()
    threads.append(t2)
    
    t3 = threading.Thread(target=find_primes, args=(30000, 20001))
    t3.start()
    threads.append(t3)
    
    for thr in threads:
        thr.join()
    print(f'{time.perf_counter() - start:.2f} sec.')
    
    
    start = time.perf_counter() 
    p1 = multiprocessing.Process(target=find_primes, args=(10000, 3)) 
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    print(f'{time.perf_counter() - start:.2f} sec.')

