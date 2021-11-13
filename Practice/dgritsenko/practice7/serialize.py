import pickle
import random
from pprint import pprint


class Human:
    _names_male = ['Liam', 'Bob', 'Tom', 'Bill', 'Jack', 'John']
    _names_female = ['Anna', 'Ezra', 'Emma', 'Luna', 'Ella', 'Mila']
    _names = _names_male + _names_female
    _countries = ['Russia', 'Australia', 'Spain', 'Italy', 'USA', 'China']
    _food_list = ['Milk', 'Juice', 'Apple', 'Potato', 'Pizza', 'Burger', 'Chocolate', 'Soup']
    _animals = ['Dog', 'Cat', 'Hamster', 'Lion', 'Tiger', 'Elephant']

    def __init__(self):
        self.name = random.choice(self._names)
        self.country = random.choice(self._countries)
        self.age = random.randint(0, 100)
        self.fathers_name = random.choice(self._names_male)
        self.mothers_name = random.choice(self._names_female)
        self.month_born = random.randint(1, 12)
        self.day_born = random.randint(1, 7)
        self.hour_born = random.randint(1, 24)
        self.favourite_food = random.choice(self._food_list)
        self.favourite_animal = random.choice(self._animals)


def create_and_save(path_to_file, count):
    i = 0
    while i < count:
        h = Human()
        with open("dumpfile", "ab") as f:
            pickle.dump(h, f, protocol=pickle.HIGHEST_PROTOCOL)
        i += 1


def read_and_print(path_to_file, count):
    i = 0
    while i < count:
        with open(path_to_file, "rb") as f:
            obj = pickle.load(f)
        pprint(vars(obj))
        i += 1


file = "dumpfile"
objects_cnt = 10

create_and_save(file, objects_cnt)
read_and_print(file, objects_cnt)
