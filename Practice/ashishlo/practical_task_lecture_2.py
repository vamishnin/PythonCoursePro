# Написать и вызвать функцию, принимающую два числа и выводящую на экран большее из двух.
# Написать и вызвать функцию, принимающую два числа и возвращающую большее из двух.
# Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.

def print_max_of_two(a, b):
    if a > b:
        print(f"the bigest one is: {a}")
    elif b > a:
        print(f"the bigest one is: {b}")
    else:
        print("numbers are equal")


def return_max_of_two(a,b):
    if a > b:
        return a
    else:
        return b


print_max_of_two(1000, 20)
print(return_max_of_two(10, 20))


class Tank:
    armor = 0
    shells = 0

    def move(self):
        pass

    def get_tank_condition(self):
        return [self.shells, self.armor]


t_34 = Tank()
t_34.armor = int(input('Please, enter armor level: '))
t_34.shells = int(input('Please, enter shells level: '))

m41_a3 = Tank()
m41_a3.armor = 100
m41_a3.shells = 64

print(f'condition of t_34: {t_34.get_tank_condition()}')
print(f'condition of m41_a3: {m41_a3.get_tank_condition()}')

