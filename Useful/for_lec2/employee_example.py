def fun(a, b):
    print(a + b)


class Employee:
    __slots__ = ('name', 'surname')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @staticmethod
    def say_hello():
        print(f'says Hello!')


e1 = Employee('Ivan', 'Ivanov')
#print(e1.__dict__)
print(e1.name)
print(e1.surname)
Employee.say_hello()

