class Parent:
    __num = 0

    def __new__(cls):
        cls.__num += 1
        return super().__new__(cls)

    @classmethod
    def get_num_of_objects(cls):
        return cls.__num  # Child._Parent__num


class Child(Parent):
    __num = 0

print(Parent._Parent__num)
p1 = Parent()
print(Parent._Parent__num)
p2 = Parent()
print(Parent._Parent__num)
c1 = Child()
print(Child._Child__num)
print(Parent.get_num_of_objects())  # 2 Parent objects
print(Child.get_num_of_objects())   # 1 Child object
