class Tank:   # Объявил класс
    def __init__(self, command, model, quantity, shot, armor):   # Задал конструктор класса
        self.command = command    # Прописал аргументы объектов
        self.model = model
        self.quantity = quantity
        self.shot = shot
        self.armor = armor

    def get_info(self):     # 1й метод класса - вывод инф-ции о команде
        print(f'Команда {self.command}: танк: {self.model}, число танков: {self.quantity},\n '
              f'сила выстрела: {self.shot}, броня: {self.armor}')

    def team_power(self):   # 2й метод класса - расчет силы команды
        power = (self.armor + self.shot) * self.quantity
        return power


tank1 = Tank('"Красные"', 'T-34', 3, 2, 5)    # объявляю 2 объекта класса и присваиваю их переменным tank1 и tank2
tank2 = Tank('"Синие"', 'Panther', 2, 3, 6)

tank1.get_info()    # вызываю метод получить информацию
print()
tank2.get_info()
print()

if (tank1.team_power()) > (tank2.team_power()):    # сравниваю силы команд
    print(f'Команда {tank1.command} сильнее')
elif (tank1.team_power()) < (tank2.team_power()):
    print(f'Команда {tank2.command} сильнее')
else:
    print(f'силы команд {tank1.command} и {tank2.command} равны')
