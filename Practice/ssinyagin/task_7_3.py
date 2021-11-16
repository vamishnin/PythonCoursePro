import random
import pickle

"""
Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.). 
Написать функцию, которая создавала бы указанное количество экземпляров, 
сериализовывала их и сохраняла в файл human.data, и другую 
функцию, которая бы читала файл human.data, десериализовывала его содержимое и 
выводила результат на печать. 
Примечание: чтоб у экземпляров Human были разные значения атрибутов, 
можно воспользоваться функциями random.randint() и random.choice(). 
"""
class Human:

    def __init__(self):
        self.__name = random.choice(['Fu', 'Yae', 'Bronya', 'Raiden', 'Kiana', 'Rita', 'Liliya', 'Rozaliya', 'Seele'])
        self.__sn = random.choice(['Kaslana', 'Rosseweisse', 'Zaychik', 'Mei', 'Hua', 'Olenyeva', 'Vollerei', 'Sakura'])
        self.__age = random.randint(17, 25)
        self.__city = random.choice(['Tokio', 'Naragosa', 'Moskou', 'New York', 'London', 'Paris'])
        self.__work = random.choice(['Valkirya', 'Principial', 'Maid', 'Cook', 'biker', 'Professor'])

    def __repr__(self):
        return f'{self.__name} {self.__sn} {self.__age} {self.__city} {self.__work}'


def createData(value):
    with open('human.data', 'wb') as f:
        valk = list()
        for i in range(value):
            a = str(Human())
            print(f'Valkyrja{i} {a}')
            valk.append(a.split(' '))
       #print('ser', valk)
        pickle.dump(valk, f, protocol=pickle.HIGHEST_PROTOCOL)

def parsData():
    with open('human.data', 'rb') as f:
        valks = pickle.load(f)
        print(valks)

#if __name__ == "__main__":
m = createData(5)
parsData()


#dd = Human()
#print(dd.dbg())




