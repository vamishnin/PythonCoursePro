import os.path
import pickle
import random


class Human:
    def __init__(self, name, surname, gender, years, location):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.years = years
        self.location = location

    def __repr__(self):
        return f'{self.name=} {self.surname=}, {self.gender=}, {self.years=}, {self.location=}'


def human_creator(num, filepath):
    names = ('Olya', 'Masha', 'Glasha', 'Katya', 'Tanya')
    surnames = ('Ivanova', 'Petrova', 'Sidorova', 'Romanova', 'Vasileva')
    genders = ('female', 'other')
    years = ('18', '21', '30', '88', '100')
    locations = ('Moscow', 'SPB', 'New York', 'Nizhny Novgorod', 'Novosibirsk')

    with open(filepath, 'bw') as f:
        for i in range(num):
            human = Human(random.choice(names), random.choice(surnames), random.choice(genders),
                          random.choice(years), random.choice(locations))
            pickle.dump(human, f)


def human_loader(filepath):
    if os.path.exists(filepath):
        humans = []
        with open(filepath, 'br') as f:
            while True:
                try:
                    humans.append(pickle.load(f))
                except EOFError:
                    break

        for each in humans:
            print(each)


human_creator(5, 'human.data')
human_loader('human.data')
