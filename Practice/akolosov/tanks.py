class Tank:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.health = 100
        self.strength = 5

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        print(f'New position is {self.x},{self.y}')
        return None

    def fire(self, delta_x, delta_y):
        target_x = self.x + delta_x
        target_y = self.y + delta_y
        print(f'Fire to point {target_x},{target_y}')
        return None

    def get_health(self):
        print(f'The health is {self.health}')
        return self.health

    def get_position(self):
        print(f'The position is {self.x},{self.y}')
        return None


me = Tank(1, 5)
me.get_position()
friend = Tank(1, 50)
friend.get_position()
enemy = Tank(300, 5)
me.move(10, 10)
friend.move(5, -10)
enemy.fire(-299, 0)
