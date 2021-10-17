class Tank:
    """
    Base tank class
    """

    _DAMAGE_VALUE = 90

    def __init__(self,
                 model="T-34",
                 weight_t=30,
                 width_mm=3000,
                 height_mm=2405,
                 length_mm=5920):
        self.__health = 100
        self.__is_alive = True
        self.__model = model
        self.weight_t = weight_t
        self.width_mm = 3000
        self.height_mm = 2405
        self.length_mm = 5920

    def attack(self, other):
        print(f"Tank {self.__model} attacks tank {other.get_model()}!")
        other.decrease_health(Tank._DAMAGE_VALUE)

    def move_to_point(self, x, y):
        print(f"Tank {self.__model} moves to point x = {x}, y = {y}!")

    def get_health(self):
        return self.__health

    def get_model(self):
        return self.__model

    def decrease_health(self, delta):
        if self.__is_alive:
            self.__health -= delta
            if self.__health < 0:
                self.__is_alive = False

    def is_alive(self):
        return self.__is_alive


# Main
t1 = Tank()
t2 = Tank("PzKpfw IV", 20, 2900, 2650, 5600)

print(f"tank {t2.get_model()} has health = {t2.get_health()}")
t1.attack(t2)
print(f"tank {t2.get_model()} has health = {t2.get_health()} after attack by {t1.get_model()}")

