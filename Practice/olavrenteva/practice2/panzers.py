class Panzer:
    """
    Class representing a panzer.

    Attributes:

    - :class:`int` __max_armor_power: max level of armor applicable to objects of this class
    - :class:`int` __max_ammunition: max count of bullets applicable to objects of this class
    - :class:`int` __max_fire_power: max count of bullets that object of this class can use simultaneously
    - :class:`int` __armor_power: current armor level of class object
    - :class:`int` __ammunition: current bullets count of class object

    Methods:

    - get_max_armor_power(): returns max level of armor applicable to objects of this class
    - get_max_ammunition(): returns max count of bullets applicable to objects of this class
    - get_max_fire_power(): returns max count of bullets that object of this class can use simultaneously
    - get_armor_power(self): returns current armor level of class object
    - get_ammunition(self): returns current bullets count of class object
    - damage(self, power): reduces current armor level of class object by 'power' points
    - repair(self, power): increases current armor level of class object by 'power' points
    - fire(self, count): reduces current bullets count of class object by 'count' point
    - add_ammunition(self, count): increases current bullets count of class object by 'count' point
    """

    __max_armor_power = 10
    __max_ammunition = 150
    __max_fire_power = 3

    def __init__(self, armor_power=5, ammunition=100):
        """
        Constructor sets initial armor level and bullets count of an object, has default values.

        :param armor_power: armor level of an object
        :param ammunition: bullets count of an object
        """
        if 0 < armor_power <= Panzer.__max_armor_power:
            self.__armor_power = armor_power
        else:
            self.__armor_power = Panzer.__max_armor_power

        if 0 < ammunition <= Panzer.__max_ammunition:
            self.__ammunition = ammunition
        else:
            self.__ammunition = Panzer.__max_ammunition

    @classmethod
    def get_max_armor_power():
        """
        :return: returns max possible armor level
        """
        return Panzer.__max_armor_power

    @classmethod
    def get_max_ammunition():
        """
        :return: returns max possible bullets count
        """
        return Panzer.__max_ammunition

    @classmethod
    def get_max_fire_power():
        """
        :return: returns max possible bullets count that can be used simultaneously
        """
        return Panzer.__max_fire_power

    def get_armor_power(self):
        """
        :return: returns current armor level
        """
        return self.__armor_power

    def get_ammunition(self):
        """
        :return: returns current bullets count
        """
        return self.__ammunition

    def damage(self, power):
        """
        Reduces current armor level of an object by 'power' points
        or sets to 0 to avoid negative value in armor_power.

        :param power: damage power, current armor level should be decreased by this number
        :return: returns current armor level
        """
        power = max(power, 0)
        self.__armor_power = max(self.__armor_power - power, 0)
        return self.__armor_power

    def repair(self, power):
        """
        Increases current armor level of an object by 'power' points
        or sets to max_armor_power to don't exceed the limit. Does nothing
        if the panzer is completely destroyed (current armor level is 0).

        :param power: repair power, current armor level should be increased by this number
        :return: returns current armor level
        """
        if self.__armor_power > 0:
            power = max(power, 0)
            self.__armor_power = min(self.__armor_power + power, Panzer.__max_armor_power)
        return self.__armor_power

    def fire(self, count):
        """
        Reduces current bullets count of an object by 'count' or less points
        depending on how many bullets are available.

        :param count: number of bullets that should be used
        :return: real number of used bullets
        """
        count = max(count, 0)
        real_count = min(min(count, Panzer.__max_fire_power), self.__ammunition)
        self.__ammunition -= real_count
        return real_count

    def add_ammunition(self, count):
        """
        Increases current bullets count of an object by 'count' or less points
        depending on available capacity.

        :param count: number of bullets that should be added
        :return: real number of added bullets
        """
        count = max(count, 0)
        real_count = min(count, Panzer.__max_ammunition - self.__ammunition)
        self.__ammunition += real_count
        return real_count


if __name__ == "__main__":
    print(f'Max possible level of armor is {Panzer.get_max_armor_power()}')
    print(f'Max possible count of bullets is {Panzer.get_max_ammunition()}')
    print(f'Max possible power of fire is {Panzer.get_max_fire_power()}')

    # creating panzer with default parameters values
    panzer1 = Panzer()
    print('\n')
    print(f'Armor level of panzer1 is {panzer1.get_armor_power()}')
    print(f'Bullets count of panzer1 is {panzer1.get_ammunition()}')

    # creating panzer with not default parameters values
    panzer2 = Panzer(7, 5)
    print('\n')
    print(f'Armor level of panzer2 is {panzer2.get_armor_power()}')
    print(f'Bullets count of panzer2 is {panzer2.get_ammunition()}')

    # creating panzer with parameters values exceeding max values
    panzer3 = Panzer(15, 200)
    print('\n')
    print(f'Armor level of panzer3 is {panzer3.get_armor_power()}')
    print(f'Bullets count of panzer3 is {panzer3.get_ammunition()}')

    # reduce armor level of panzer1 by 3 (from 5)
    print('\n')
    print(f'Armor level of panzer1 before change is {panzer1.get_armor_power()}')
    panzer1.damage(3)
    # print changed armor level of panzer1 using get method
    print(f'Armor level of panzer1 is {panzer1.get_armor_power()}')

    # attempt to reduce armor level of panzer1 by 3 (from 2) and
    # printing the returned value (changed armor level)
    print('\n')
    print(f'Armor level of panzer1 before change is {panzer1.get_armor_power()}')
    print(f'Armor level of panzer1 is {panzer1.damage(3)}')

    # attempt to reduce armor level of panzer2 by -1 (from 7) and
    # printing the returned value
    print('\n')
    print(f'Armor level of panzer2 before change is {panzer2.get_armor_power()}')
    print(f'Armor level of panzer2 is {panzer2.damage(-1)}')

    # increase armor level of panzer2 by 2 (from 7)
    print('\n')
    print(f'Armor level of panzer2 before change is {panzer2.get_armor_power()}')
    panzer2.repair(2)
    print(f'Armor level of panzer2 is {panzer2.get_armor_power()}')

    # attempt to increase armor level of panzer2 by 3 (from 9) and
    # printing the returned value (changed armor level)
    print('\n')
    print(f'Armor level of panzer2 before change is {panzer2.get_armor_power()}')
    print(f'Armor level of panzer2 is {panzer2.repair(3)}')

    # attempt to increase armor level of panzer2 by -5 (from 10) and
    # printing the returned value
    print('\n')
    print(f'Armor level of panzer2 before change is {panzer2.get_armor_power()}')
    print(f'Armor level of panzer2 is {panzer2.repair(-5)}')

    # attempt to increase armor level of panzer1 by 5 (from 0) and
    # printing the returned value
    print('\n')
    print(f'Armor level of panzer1 before change is {panzer1.get_armor_power()}')
    print(f'Armor level of panzer1 is {panzer1.repair(5)}')

    # reduce bullets count of panzer1 by 2 (from 100) and printing really used bullets
    print('\n')
    print(f'Bullets count of panzer1 before change is {panzer1.get_ammunition()}')
    print(f'Panzer1 used {panzer1.fire(2)} bullets')
    print(f'Bullets count of panzer1 is {panzer1.get_ammunition()}')

    # attempt to reduce bullets count of panzer2 by 20 (from 5) and
    # printing really used bullets
    print('\n')
    print(f'Bullets count of panzer2 before change is {panzer2.get_ammunition()}')
    print(f'Panzer2 used {panzer2.fire(20)} bullets')
    print(f'Bullets count of panzer2 is {panzer2.get_ammunition()}')

    # attempt to reduce bullets count of panzer2 by 3 (from 2) and
    # printing really used bullets
    print('\n')
    print(f'Bullets count of panzer2 before change is {panzer2.get_ammunition()}')
    print(f'Panzer2 used {panzer2.fire(3)} bullets')
    print(f'Bullets count of panzer2 is {panzer2.get_ammunition()}')

    # attempt to reduce bullets count of panzer2 by -100 (from 0) and
    # printing really used bullets
    print('\n')
    print(f'Bullets count of panzer2 before change is {panzer2.get_ammunition()}')
    print(f'Panzer2 used {panzer2.fire(-100)} bullets')
    print(f'Bullets count of panzer2 is {panzer2.get_ammunition()}')

    # add 10 bullets to panzer1 (from 98)
    print('\n')
    print(f'Bullets count of panzer1 before change is {panzer1.get_ammunition()}')
    print(f'Panzer1 got {panzer1.add_ammunition(10)} bullets')
    print(f'Bullets count of panzer1 is {panzer1.get_ammunition()}')

    # attempt to add 50 bullets to panzer1 (from 108)
    print('\n')
    print(f'Bullets count of panzer1 before change is {panzer1.get_ammunition()}')
    print(f'Panzer1 got {panzer1.add_ammunition(50)} bullets')
    print(f'Bullets count of panzer1 is {panzer1.get_ammunition()}')

    # attempt to add -100 bullets to panzer2 (from 0)
    print('\n')
    print(f'Bullets count of panzer2 before change is {panzer2.get_ammunition()}')
    print(f'Panzer2 got {panzer2.add_ammunition(-100)} bullets')
    print(f'Bullets count of panzer2 is {panzer2.get_ammunition()}')





