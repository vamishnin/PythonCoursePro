class A:
    def __add__(self, other):
        self.called = True


def fun(a, b):
    print(a + b)


a = A()
b = A()
fun(a, b)
a.called = False
assert a.called
assert not hasattr(b, 'called')
