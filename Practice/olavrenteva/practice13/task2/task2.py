class Money:
    _rate_to_dollar = None

    def __init__(self, ruble, penny=0):
        self.ruble = ruble
        self.penny = penny

    @property
    def ruble(self):
        return self._ruble

    @ruble.setter
    def ruble(self, ruble):
        if not isinstance(ruble, int):
            raise ValueError('ruble should be integer')
        self._ruble = ruble

    @property
    def penny(self):
        return self._penny

    @penny.setter
    def penny(self, penny):
        if not isinstance(penny, int) or penny < 0 or penny > 99:
            raise ValueError('penny should be natural number and should not exceed 99')
        self._penny = penny

    def __str__(self):
        return f'{self.ruble},{self.penny}' if self.penny >= 10 else f'{self.ruble},0{self.penny}'

    def __add__(self, other):
        rub = self.ruble + other.ruble + (self.penny + other.penny) // 100
        pen = (self.penny + other.penny) % 100
        return Money(rub, pen)

    def __sub__(self, other):
        if self < other:
            return -(other - self)

        if self.penny >= other.penny:
            rub = self.ruble - other.ruble
            pen = self.penny - other.penny
        else:
            rub = self.ruble - other.ruble - 1
            pen = 100 + self.penny - other.penny
        return Money(rub, pen)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            rub = int(other)
            pen = int((other - int(other)) * 100)
            return self / Money(rub, pen)
        else:
            div_res = (self.ruble * 100 + self.penny) / (other.ruble * 100 + other.penny)
            rub = int(div_res)
            pen = int((div_res - rub) * 100)
            return round(div_res, 2)

    def __eq__(self, other):
        return self.ruble == other.ruble and self.penny == other.penny

    def __lt__(self, other):
        return self.ruble < other.ruble or (self.ruble == other.ruble and self.penny < other.penny)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other < self or other == self

    def __neg__(self):
        return Money(-self.ruble, self.penny)

    def convert_to_dollars(self):
        if not Money._rate_to_dollar:
            raise Exception('rate to dollar is not defined')

        return (self.ruble + self.penny / 100) * Money._rate_to_dollar

    @classmethod
    def get_rate_to_dollar(cls):
        return cls._rate_to_dollar

    @classmethod
    def set_rate_to_dollar(cls, rate_to_dollar):
        if not isinstance(rate_to_dollar, float) or rate_to_dollar <= 0:
            raise ValueError('rate_to_dollar should be natural number')
        cls._rate_to_dollar = rate_to_dollar

    @classmethod
    def clear_rate_to_dollar(cls):
        cls._rate_to_dollar = None
