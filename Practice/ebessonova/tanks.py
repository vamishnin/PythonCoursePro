class Tank:
    coordinates = [0, 0]
    id = 0

    def __init__(self, x, y):
        self.coordinates = [x, y]

    def move(self, x, y):
        self.coordinates = [x, y]

    def due(self):
        self.coordinates = [0, 0]

    def is_alive(self):
        if self.coordinates != [0, 0]:
            return True
        return False

    def get_position(self):
        return self.coordinates


def run():
    '''
    Функция для проверки методов класса Tank
    задает координаты двух объектов Tank,
    позводяет выбрать координыты одного из них несколько раз,
    пока эти координаты не совпадут с координатами второго объекта Tank,
    в этом случае координаты воторого объекта обнуляются.
    Выводится в консоль резульат проверки координат.
    :return:
    '''
    tank1 = Tank(2, 3)
    tank2 = Tank(5, 4)

    while 1:
        new_coord_x = input('Move tank x ')
        if new_coord_x == 'stop':
            break
        new_coord_y = input('Move tank y ')
        if new_coord_y == 'stop':
            break

        tank1.move(int(new_coord_x), int(new_coord_y))

        if tank2.get_position() == tank1.get_position():
            tank2.due()
            break

    if tank1.is_alive():
        print('Tank1 is alive')
    else:
        print('Tank1 is dead')

    if tank2.is_alive():
        print('Tank2 is alive')
    else:
        print('Tank2 is dead')


run()


