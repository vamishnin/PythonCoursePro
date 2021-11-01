class Tank:
    def __init__(self, model, weight, brunt, fire):
        self.__model = model
        self.__weight = weight
        self.__brunt = brunt
        self.__fire = fire

    def get_tank_info(self):
        print(f'The tank is {self.__model}, weight {self.__weight} kg, brunt {self.__brunt} units, '
                  f'fire {self.__fire} shot per min')


tank1 = Tank('MC-1', 240, 215, 62)
tank1.get_tank_info()

