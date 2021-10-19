import time
import datetime
import random


class TimeMeasurement:
    def __enter__(self):
        # monotonic_ns returns nanoseconds
        self.__begin = time.monotonic_ns()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # get time difference and convert nanoseconds to microseconds
        delta = (time.monotonic_ns() - self.__begin) / 1000
        print(f"It takes {str(datetime.timedelta(microseconds=delta))} Exception type: {exc_type}")


if __name__ == "__main__":
    with TimeMeasurement():
        time.sleep(random.randint(3, 6))
