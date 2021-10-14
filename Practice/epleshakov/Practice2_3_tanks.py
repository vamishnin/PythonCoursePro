class Tank:
    '''Танк,
        Двигается вперед и назад (move_forward() и move_backward())
        Поворачивает вправо(rotate_right()) и  влево(rotate_left()) строго по направлениям
        Стреляет fire() с уменьшением боезапаса
        Урон сохраняется при вызове функции take_damage()
    '''

    def __init__(self, x, y):  # Определим общий конструктор
        self.x = x
        self.y = y
        self.dead = False
        self.health = 100
        self.power = 20
        self.ammo = 10
        self.directions = ['up', 'right', 'down', 'left']
        self.current_direction = 0

    def move_forward(self):
        if self.dead:
            print('Эту гору хлама не сдвинуть! Нас подбили!!!')
        else:
            if self.current_direction == 0:
                self.y += 1
            elif self.current_direction == 1:
                self.x += 1
            elif self.current_direction == 2:
                self.y -= 1
            elif self.current_direction == 3:
                self.x -= 1

    def move_backward(self):
        if self.dead:
            print('Назад не поедет! Нас подбили!!!')
        else:
            if self.current_direction == 0:
                self.y -= 1
            elif self.current_direction == 1:
                self.x -= 1
            elif self.current_direction == 2:
                self.y += 1
            elif self.current_direction == 3:
                self.x += 1

    def rotate_right(self):
        if self.dead:
            print('И не поворачивается ! Нас подбили!!!')
        else:
            if self.current_direction < 3:
                self.current_direction += 1
            else:
                self.current_direction = 0

    def rotate_left(self):
        if self.dead:
            print('И туда не поворачивается ! Нас подбили!!!')
        else:
            if self.current_direction <= 0:
                self.current_direction = 3
            else:
                self.current_direction -= 1

    def fire(self):
        if self.ammo:
            self.ammo -= 1
            print('Бабах!!!')
        else:
            print('Снаряды кончились, нужна перезарядка!!!')

    def reload(self):
        self.ammo = 10
        print('Перезарядка окончена!')

    def take_damage(self, power):
        self.health = self.health - power
        print(f'Получен урон: {power}')
        if self.health <= 0:
            self.dead = True
            print('Танк подбит!!!')


# Создадим два экземпляра Танка и посмотрим где он стоит и куда направлен
Leopard = Tank(0, 0)
Leopard.health = 200
Panzer = Tank(10, 20)
print(Leopard.directions[Leopard.current_direction])
print(Leopard.x)
print(Leopard.y)
# Покатаемся по кругу вправо
i = 0
while i <= 5:
    print('Current direction:' + Leopard.directions[Leopard.current_direction])
    Leopard.rotate_right()
    Leopard.move_forward()
    Leopard.move_forward()
    Leopard.move_forward()
    print(f'x: {Leopard.x}')
    print(f'y: {Leopard.y}')
    print('direction on stop:' + Leopard.directions[Leopard.current_direction])
    i += 1
# И покатаемся по кругу влево задом
i = 0
while i <= 5:
    print('Current direction:' + Leopard.directions[Leopard.current_direction])
    Leopard.rotate_left()
    Leopard.move_backward()
    Leopard.move_backward()
    Leopard.move_backward()
    print(f'x: {Leopard.x}')
    print(f'y: {Leopard.y}')
    print('direction on stop:' + Leopard.directions[Leopard.current_direction])
    i += 1
# Стрельнем и получим смертельный урон
print(Leopard.__dict__)
Leopard.fire()
print(Leopard.__dict__)
Leopard.fire()
print(Leopard.__dict__)
Leopard.take_damage(30)
print(f'Health: {Leopard.health}')
Leopard.take_damage(90)
print(f'Health: {Leopard.health}')
print('Подбит?: ' + str(Leopard.dead))
Leopard.take_damage(90)
print(f'Health: {Leopard.health}')
print(Leopard.dead)
# Попробуем сдвинуться или повернуться
Leopard.move_forward()
Leopard.rotate_right()

# Повернем и проверим где Танк B
print(Panzer.__dict__)
Panzer.rotate_right()
print('Current direction:' + Panzer.directions[Panzer.current_direction])
Panzer.rotate_right()
Panzer.move_forward()
print(f'x: {Panzer.x}')
print(f'y: {Panzer.y}')
print(f'Health: {Panzer.health}')
print('direction on stop:' + Panzer.directions[Panzer.current_direction])