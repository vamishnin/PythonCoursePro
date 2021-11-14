import time


class Timecalc:

    def __init__(self):
        pass

    def __enter__(self):
        self.starttime = time.time()

    def __exit__(self, exception_type, exception_value, traceback):
        self.endtime = time.time()
        self.res = self.endtime - self.starttime
        print(self.res)

def content(value):
    m = value * 100
    time.sleep(3)
#    print(m)

with Timecalc():
    b = content(5)
