import pickle
import json


class User:
    def __init__(self):
        self._name = 'name'
        self._age = 'age'

    def set_name(self, value):
        self._name = value

    def get_name(self):
        return self._name

    def set_age(self, value):
        self._age = value

    def get_age(self):
        return self._age

class Worker(User):
    def __init__(self):
        super().__init__()
        self._salary = 0

    def set_salary(self, number):
        self._salary = number

    def get_salary(self):
        return self._salary

    def __str__(self):
        return f"Worker: name={self._name}, age={self._age}, salary={self._salary}"


john = Worker()
john.set_name('John')
john.set_age(25)
john.set_salary(1000)
jack = Worker()
jack.set_name('Jack')
jack.set_age(26)
jack.set_salary(2000)

with open("dumpfile", "wb") as f:
    pickle.dump(john, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(jack, f, protocol=pickle.HIGHEST_PROTOCOL)
