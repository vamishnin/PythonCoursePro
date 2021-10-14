'''
Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
'''
import time

class CtxTimer: 
    
    def __enter__(self): 
        self._enter_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._exit_time =  time.time() - self._enter_time
        print(f'Your code exec time: {self._exit_time}')


def factorial(n):
    if n <= 1:
        return 1
    else: 
        return n * factorial(n-1)

if __name__ == '__main__':

    with CtxTimer():
        factorial(50)
