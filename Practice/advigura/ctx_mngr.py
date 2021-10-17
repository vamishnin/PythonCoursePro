import time

class TimeContextManager:
    def __enter__(self):
        self.__start_time = time.monotonic()
        print(f'started at {self.__start_time}')
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        current_time = time.monotonic()
        print(f'finished at {current_time}')
        print(f'elapsed time {current_time - self.__start_time}')
    
with TimeContextManager(): time.sleep(3)