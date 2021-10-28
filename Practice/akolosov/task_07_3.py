import random as r
import pickle


FILE_NAME = "Practice/akolosov/human.data"


class Human:

    def __init__(self, name: str, secondname: str, surname: str, age: int, address: str):
        self.__name = name
        self.__secondname = secondname
        self.__surname = surname
        self.__age = age
        self.__address = address

    def __repr__(self) -> str:
        return f"Name: {self.__name} {self.__secondname} {self.__surname} age: {self.__age} address: {self.__address}"


def save_humans(num: int):
    names = ["Ivan", "Petr", "Oleg", "Danila"]
    senondnames = ["Ivanivich", "Petrovich", "Olegovich", "Danilovich"]
    surnames = ["Ivanov", "Petrov", "Sidorov", "Kuznecov"]
    addresses = ["Kremlin", "Gremlin", "Omsk", "Orel"]

    people = []
    for i in range(num):
        people.append(Human(r.choice(names), r.choice(senondnames),
                      r.choice(surnames), r.randint(1,99), r.choice(addresses)))

    with open(FILE_NAME, "wb") as writer:
        for i in people:
            pickle.dump(i, writer, protocol=pickle.HIGHEST_PROTOCOL)
    return None


def restore_people():
    people = []
    with open(FILE_NAME,"rb") as reader:
        while True:
            try:
                a = pickle.load(reader)
            except EOFError:
                break
            people.append(a)
    return people


if __name__ == "__main__":
    save_humans(10)
    team = restore_people()
    for i in team:
        print(str(i))
