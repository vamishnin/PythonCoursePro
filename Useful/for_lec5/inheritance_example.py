class Position:
    def __init__(self, money):
        self.money = money


class Employee:
    def __init__(self, name, surname, salary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name
        self._surname = surname
        self._salary = salary
        self.__free_time = 0
        self._position = Position(salary)

    def say_hello(self):
        print('Hello')

    def __repr__(self):
        return f"Employee {self._name} {self._surname} with {self.__free_time}"


class ExampleBase:
    def __init__(self, attr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._attr = attr


class Player(ExampleBase):
    def __init__(self, attr, sport, *args, **kwargs):
        super().__init__(attr, *args, **kwargs)
        self._sport = sport


class Manager(Employee, Player):
    def __init__(self, name, surname, salary, employees=tuple()):
        super().__init__(name, surname, salary, 'attr', 'football')
        # Альтернативный вызов конструкторов, если в родительских
        # классах не предусмотрены вызовы super().__init__(*args, **kwargs):
        # super().__init__(name, surname, salary)
        # super(Employee, self).__init__('football')
        self._employees = employees

    def __repr__(self):
        return f"Manager {self._name} {self._surname}"


e1 = Employee("Ivan", "Ivanov", 50000)
m = Manager("Petr", "Petrov", 100000, (e1,))
print(m._sport)
print(m._attr)
