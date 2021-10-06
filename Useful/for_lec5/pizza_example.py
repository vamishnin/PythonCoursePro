class Pizza:
    name = "Pizza"

    def __init__(self):
        self._status = "no pizza"

    def prepare_base(self):
        print("base prepared")
        self._status = "base prepared"

    def add_ingr(self):
        print("no ingredients")

    def bake(self):
        print("baked")
        self._status = "ready"

    def show_status(self):
        print(f"{self.name} status {self._status}")


class MeatPizza(Pizza):
    name = "MeatPizza"

    def add_ingr(self):
        print('added meat')


class VegPizza(Pizza):
    name = "VegPizza"

    def add_ingr(self):
        print('added vegetables')


class MushPizza(Pizza):
    name = "MushPizza"

    def add_ingr(self):
        print('added mushrooms')


def make_pizza(p):
    p.prepare_base()
    p.add_ingr()
    p.bake()


pizzas = [MeatPizza(), VegPizza(), MushPizza()]
for pizza in pizzas:
    make_pizza(pizza)
    pizza.show_status()

