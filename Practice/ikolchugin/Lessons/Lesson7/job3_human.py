from random import randint, choice
import pickle


class Human:
    def __init__(self, name, surname=None, age=None,
                 city=None, street=None, building=None, apartment=None):
        self._name = name
        self._surname = surname
        self._age = age
        self._city = city
        self._street = street
        self._building = building
        self._apartment = apartment

    def __str__(self):
        return f'{self._name}, {self._surname}, {self._age} ,' \
               f' г. {self._city}, ул. {self._street}, д. {self._building}, кв. {self._apartment}'


with open('example_data.dat', 'rb') as example_dict:
    example_data = pickle.load(example_dict)


def create_humans_example(n, examples):
    with open('human.data', 'wb') as f_human_data:
        _humans_data = [
            Human(
                name=choice(examples['name']),
                surname=choice(examples['surname']),
                age=randint(23, 95),
                city=choice(examples['city']),
                street=choice(examples['street']),
                building=randint(1, 33),
                apartment=randint(1, 199),
            ) for _ in range(n)]
        pickle.dump(_humans_data, f_human_data)


create_humans_example(10, example_data)


def read_humans_data():
    with open('human.data', 'rb') as f_human_data:
        return pickle.load(f_human_data)


humans_data = read_humans_data()
for i in humans_data:
    print(i)
