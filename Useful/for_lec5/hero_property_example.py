class HeroException(Exception):
    pass


class Hero:
    def __init__(self, power):
        self.power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if isinstance(value, int):
            self._power = value
        else:
            raise HeroException(['Bad power'])

    def __add__(self, other):
        return Hero(self.power + other.power)


h = Hero("Maximum")
h.power = 200
print(h.power)
