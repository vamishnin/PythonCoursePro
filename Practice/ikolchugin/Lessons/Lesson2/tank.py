import string
from random import randrange, choice


class Tank:
    """
    Base class for tanks
    """
    def __init__(self, team='Red', label=None, armor=30, health=30, damage=5, ammo=10):
        """

        :param team: Команда, за которую выступает танк
        :param armor:   Уровень защиты
        :param health:  Уровень "здоровья" aka степень исправности
        :param damage:  Уровень оказываемого урона
        :param ammo:    Боекомплект, шт
        """
        self.team = team
        self.label = label if label is not None else self.id_generator()
        self._armor = armor
        self._health = health
        self._damage = damage
        self._ammo = ammo
        self.dead = self._health <= 0

    @staticmethod
    def id_generator(size=30, chars=string.ascii_uppercase + string.digits):
        return ''.join(choice(chars) for _ in range(size))

    def defend(self, damage):
        """

        :param damage: Нанесённый урон
        """
        if self._armor > 0:
            self._armor -= damage
        elif self._health > 0:
            self._health -= damage

        self.dead = self._health <= 0
        if self.dead:
            print(f'{self.team}_{self.label} подбит')
        else:
            print(f'{self.team}_{self.label} готов к битве')

    def attack(self, target=None):
        if type(target) is not Tank:
            print('Цель атаки не указана')
            self._ammo -= 1
        elif self.dead:
            print('Атака невозможна, танк выведен из строя')
        elif self.team == target.team:
            print('По своим, чур, не стрелять!')
            self._ammo -= 1
        else:
            print(f'{self.team}_{self.label} атакует цель: '
                  f'{target.team}_{target.label}')
            if self._ammo > 0:
                self._ammo -= 1
                target.defend(self._damage)
            else:
                print(f'Закончился боекомплект')


teams = {
    'Blue': [],
    'Green': []
}

# for t in teams:
#     for i in range(0, 5):
#         teams[t].append(Tank(t, f'Tank{i}'))
#
# print(teams.values())
# game_round = 0

t1 = Tank(team='Blue', label='Tank1', damage=14)
t2 = Tank(team='Blue', label='Tank2')
t3 = Tank(team='Green', label='Tank3', armor=12, health=30)
t4 = Tank(team='Green', label='Tank4', armor=120, health=40)
t5 = Tank(team='Yellow', armor=120, health=40)
#
#
t1.attack()
t1.attack(t2)
t1.attack(t3)
t1.attack(t3)
t1.attack(t3)
