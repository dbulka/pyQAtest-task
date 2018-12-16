import logging
from game.views.interface import GameInterface


class User(GameInterface):
    """
    part of interface, which cooperates with user
    """

    def give_food(self, pet):
        """
        change Tamagochi hunger value
        :hunger pet: Tamagochi hunger
        :return: deduct input value from Tamagochi hunger
        """
        pet.hunger -= int(input('enter amount of food: '))

    def give_hp(self,pet):
        """
        change Tamagochi hp value
        :hp pet: Tamagochi hp
        :return: deduct input value from Tamagochi hp
        """
        pet.hp  += int(input('enter amount of hp: '))

    def play(self,pet):
        """
        change Tamagochi happiness value
        :happiness pet: Tamagochi happiness
        :return: deduct input value from Tamagochi happiness
        """
        pet.happiness  += int(input('enter amount of hp: '))

    def make_choice(self, n):
        """
        give to user ways to control Tamagochi
        :param n: step number
        :return: number of way
        """
        print("""
        Choose way:
        #1 - Feed pet
        #2 - Heal pet
        #3 - Play with pet
              """)
        condition = ('1','2','3')
        resp = True
        while resp:
            choice = self.ask_question('Enter number of way: ')
            if choice in condition:
                resp = False
            else:
                resp = True
                logging.warning('you enter wrong number, repeat please')
        return choice
