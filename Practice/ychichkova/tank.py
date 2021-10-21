class Tank:
    def __init__(self, model, weight, brunt, fire):
        self.model = model
        self.weight = weight
        self.brunt = brunt
        self.fire = fire

    def get_tank_info(self):
        print(f'The tank is {self.model}, weight {self.weight} kg, brunt {self.brunt} units, '
                  f'fire {self.fire} shot per min')


tank1 = Tank('MC-1', 240, 215, 62)
tank1.get_tank_info()
