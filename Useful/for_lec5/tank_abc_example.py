from abc import ABCMeta, abstractmethod


class BaseTank(metaclass=ABCMeta):
    def __init__(self, power, speed):
        self._power = power
        self._speed = speed
        self._x = 0

    def move(self, inc):
        self._x += inc * self._speed

    @abstractmethod
    def shoot(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Tank(BaseTank):
    def show(self):
        print("I'm Tank")

    def shoot(self):
        print('Ba-bah')


class T34(BaseTank):
    def show(self):
        print("I'm T34")

    def shoot(self):
        print('Ba-ba-bah')


class Tiger(BaseTank):
    def show(self):
        print("I'm Tiger")

    def shoot(self):
        print('Bdysh')


tanks = [Tank(10, 10), T34(20, 30), Tiger(30, 10)]
tanks = [t for t in tanks if isinstance(t, BaseTank)]
print(tanks)
while True:
    idx = int(input('Input tank idx (0-2, non-digit to cancel): '))
    steps = int(input('Input step: '))
    tanks[idx].move(steps)
    tanks[idx].shoot()
    tanks[idx].show()
