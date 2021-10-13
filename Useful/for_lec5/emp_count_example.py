class Employee:
    num_of_employees = 0

    # def __new__(cls, *args, **kwargs):
    #     cls.num_of_employees += 1
    #     return super().__new__(cls)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Employee.num_of_employees += 1

    def __del__(self):
        Employee.num_of_employees -= 1


e1 = Employee("Ivan", "Ivanov")
del e1
print(Employee.num_of_employees)

