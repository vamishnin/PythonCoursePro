import time

# Practice 6 Q1
def chargen():
    while True: #  Из этого цикла не выйти
        for c in '0123456789':
            yield c


def chargen2():
    for c in '0123456789':
        yield c


words = [c + c for c in chargen2()][:10]
print(words)

# Practice 6 Q2
def multiplier(m=1, source=[1, 2, 3]):
    result = source.copy()
    for i, x in enumerate(source):
        result[i] *= m
    return result

def multiplier2(m=1, source=[1, 2, 3]): #  Сокращенный вариант multiplier()
    return [x*m for i, x in enumerate(source)]


print(multiplier2(7))
print(multiplier2(7))
print(multiplier2(7))

print(multiplier2(12, [1, 2, 3, 4, 6]))

# Practice 6 Q3
class TimeCtxMng:
    def __enter__(self):
        self._t = time.time()
        print('Starting code')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Code completed. Time to work = {time.time() - self._t} sec')
        print(f'Error info: type - {exc_type}')


with TimeCtxMng():
    time.sleep(5) # Типа нагрузка

