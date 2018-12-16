import random

class Tamagochi:
    """
    create pet with some parameters
    """

    def __init__(self, name):
        """
        initialize Tamagochi
        :param name: Tamagochi name
        """
        self.name = name
        self.hp = random.randint(0,100)
        self.hunger = random.randint(0,100)
        self.happiness = random.randint(0,100)
        self.alive = True

    def is_alive(self):
        """
        check Tamagochi alive param
        :return: Tamagochi alive param
        """
        return (0 < self.happiness < 100) and (0 < self.hp < 100) and (0 < self.hunger < 100)

    def __str__(self):
        """
        show Tamagochi variables
        """
        return print('hp: {0}| hunger: {1} | happines: {3} | alive: {4}'.format(self.hp, self.hunger, self.happiness,self.alive))
