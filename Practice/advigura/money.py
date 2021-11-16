class Money:
    def __init__(self, ruble, penny = 0):
        self._ruble = ruble
        self._penny = penny
        self.rate = 70

    def __repr__(self):
        return '{},{}'.format(self._ruble, self._penny)

    def __eq__(self, other):
        return self._ruble == other._ruble and self._penny == other._penny

    def __lt__(self, other):
        return (self._ruble * 100 + self._penny) < (other._ruble * 100 + other._penny)

    def __add__(self, other):
        res = self._ruble * 100 + self._penny + other._ruble * 100 + other._penny
        return Money(res // 100, res % 100)
    def __sub__(self, other):
        res = self._ruble * 100 + self._penny - other._ruble * 100 - other._penny
        if res >= 0:
            return Money(res // 100, res % 100)
        else:
            return Money(-(-res // 100), -res % 100)

    def __truediv__(self, other):
        return (self._ruble * 100 + self._penny) / (other._ruble * 100 + other._penny)

    def convert_to_dollar(self):
        res = (self._ruble * 100 + self._penny) / self.rate
        # print(res)
        return Money(res // 100, res % 100)


# m1 = Money(5, 10)
# m2 = Money(5, 40)
# m3 = Money(5, 10)
# m4 = Money(3, 36)
# print(m1)
# if (m1 == m2):
#     print('m1 eq m2')
# if (m1 == m3):
#     print('m1 eq m3')
# if (m1 < m2):
#     print('m1 lt m2')
# print(f'sum={m1 + m2 + m3 + m2 + m4}')
#
# print(f"sub={m1 - m4}")
# print(f"sub2={m4 - m1}")
#
# print(f'{m1/m4}')
#
# m5 = Money(140, 0)
# print(f'{m5.convert_to_dollar()}')

