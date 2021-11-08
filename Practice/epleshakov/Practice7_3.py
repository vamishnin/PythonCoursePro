# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.).
# Написать функцию, которая создавала бы указанное количество экземпляров, сериализовывала их
# и сохраняла в файл human.data, и другую функцию, которая бы читала файл human.data, десериализовывала
# его содержимое и выводила результат на печать.
# Примечание: чтоб у экземпляров Human были разные значения атрибутов, можно
# воспользоваться функциями random.randint() и random.choice().
import random
import pickle


class Human:

    def __init__(self, name = '', sec_name = '', age = 0, city = '', street = '', bulding = 0, place = 0):
        self.__name = name
        self.__sec_name = sec_name
        self.__age = age
        self.__city = city
        self.__street = street
        self.__bulding = bulding
        self.__place = place

    def __repr__(self):
        return(f'Name: {self.__name}, Second name: {self.__sec_name}, Age: {self.__age}, '
              f'City: {self.__city}, Street: {self.__street}, '
              f'Bulding: {self.__bulding}, Place: {self.__place}')


def serialize_humans(hum_num):
    with open('human.data', 'wb') as file:
        nn = 0
        hum = []
        while nn < hum_num:
            names = random.choice(['Ivan', 'Petr', 'Oleg', 'Fedr', 'Alex'])
            sec_names = random.choice(['Ivanov', 'Petrov', 'Boshirov', 'Sidorov'])
            citys = random.choice(['Moskow', 'NNovgorod', 'Novosibirsk', 'Samara'])
            streets = random.choice(['1-lane', '2-lane', '3-lane'])
            ages = random.randint(1, 100)
            buldings = random.randint(1, 20)
            places = random.randint(1, 500)
            hum.append(Human(names, sec_names, ages, citys, streets, buldings, places))
            nn += 1
        pickle.dump(hum, file, protocol=pickle.HIGHEST_PROTOCOL)

def deserialise_human_data():
    with open('human.data', 'rb') as file:
        return pickle.load(file)


serialize_humans(16)
humans = deserialise_human_data()
for h in humans:
    print(h)
