
class Tank:  # объявляем класс

    def __init__(self, model, strength, power, damage):  # задаем конструктор класса
        self.model = model
        self.strength = strength
        self.power = power
        self.damage = damage

    def description(self): # объявляем 1й метод класса (вывод информации о танках)
        print(f'Модель танка: {self.model}, прочность: {self.strength}, мощность: {self.power}, урон: {self.damage}')

    def improve(self):  # объявляем 2й метод класса (улучшение характеристик танков, вывод новой информации)
        for attr in self.__dict__:
            value = getattr(self, attr)
            if value.isalpha():
                setattr(self, attr, value.upper())
            else:
                setattr(self, attr, int(value) * 2)
        print(f'Модель танка: {self.model} улучшена: \nновая прочность: {self.strength}, \nновая мощность: {self.power}, \nновый урон: {self.damage}')


# создаем экземпляры класса:
tank1 = Tank('Valentine', '580', '9', '47')
tank2 = Tank('Tetrarch', '280', '25', '45')
# вызываем 1й метод класса
tank1.description()  # то же самое, что и Tank.description(tank1)
tank2.description()
# вызываем 2й метод класса
tank1.improve()
tank2.improve()

