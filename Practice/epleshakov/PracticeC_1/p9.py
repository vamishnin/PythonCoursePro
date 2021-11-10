# Создайте класс User, в котором будут следующие поля: name (имя), age (возраст),
#  методы setName, getName, setAge, getAge.
# Создайте класс Worker, который наследуется от класса User и имеет дополнительное поле salary (зарплата),
#   а также методы getSalary и setSalary.
# Создайте объект этого класса name='John', age=25, salary=1000.
# Создайте второй объект этого класса 'Jack', age=26, salary=2000. Найдите сумму зарплат объектов John и Jack.

class User():
    def __init__(self, name, age):
        self.h_name = name
        self.h_age = age

    def getName(self):
        return self.h_name

    def getAge(self):
        return self.h_age

    def setName(self, input_name):
        self.h_name = input_name

    def setAge(self, input_age):
        self.h_age = input_age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setSalary(self, input_salary):
        self.salary = input_salary


w1 = Worker(name='John', age=25, salary=1000)
w2 = Worker(name='Jack', age=26, salary=2000)
if w1.salary > w2.salary:
    print(f'{w1.h_name} больше {w2.h_name}')
else:
    print(f'{w1.h_name} меньше {w2.h_name}')