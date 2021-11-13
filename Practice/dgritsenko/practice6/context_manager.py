import time

PAUSE_DURATION_SEC = 1


class TimeManager:

    def __init__(self):
        self._tic = 0
        self._toc = 0

    def __enter__(self):
        self._tic = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._toc = time.perf_counter()
        print(f"Код выполнялся {self._toc - self._tic:0.4f} секунд")

if __name__ == '__main__':
    with TimeManager():
        print("Tic")
        time.sleep(PAUSE_DURATION_SEC)
        print("Toc")
