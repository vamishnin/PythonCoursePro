import random
import pickle


class Human:
    def __init__(self):
        self.__name = random.choice(['Ivan', 'Petr', 'Egor', 'Eugene'])
        self.__surname = random.choice(['Ivanov', 'Petrov', 'Sidorov', 'Nikolaev'])
        self.__age = random.randint(20, 50)
        self.__city = random.choice(['Dzerzhinsk', 'Bor', 'Kstovo', 'Pavlovo'])
        self.__index = random.randint(606000, 608000)
        self.__card_number = random.randint(1000000, 9999999)


def serialize_human(human_amount):
    with open('human.data', 'wb') as f:
        idx = 0
        humans = list()
        while idx < human_amount:
            humans.append(Human())
            idx += 1
        pickle.dump(humans, f, protocol=pickle.HIGHEST_PROTOCOL)


def deserialize_human():
    with open('human.data', 'rb') as f:
        return pickle.load(f)


serialize_human(5)

print(deserialize_human())
