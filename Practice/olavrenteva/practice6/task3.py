import time
import requests


class ExecutionTimeMeter:
    def __enter__(self):
        self._start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exec_time = time.time() - self._start_time
        print(f"Execution time is {self.exec_time}")


def get_page(url):
    page = requests.get(url)


with ExecutionTimeMeter():
    get_page("https://www.gosuslugi.ru/")
