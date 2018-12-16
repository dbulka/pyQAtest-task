from game.models import Tamagochi, random, pets


class GameInterface:
    """
    part of interface, which show
    """

    def show_tamagochi(self, pet):
        """
        show Tamagochi state (param)
        :return: string with Tamagochi param
        """
        print('hp: {0}| hunger: {1} | happines: {2} | alive: {3} | name is {4}'.format(pet.hp, pet.hunger, pet.happiness, pet.alive, pet.name))

    def show_game_result(self,n,alive):
        """
        show game result
        :param n: number of steps
        :param alive: state of Tamagochi alive
        :return: string with game result
        """
        print('%s on %s th step' % ('YOU WIN!' if (alive and n > 100) else 'YOU LOSE!', n))


    def choose_pet(self):
        tamagochs = [pets.Cat(), pets.Dog(), pets.Rabbit(), pets.Bird(), pets.Dragon()]
        x = random.randrange(0,len(tamagochs))
        pet = tamagochs[x]
        # print(pet)
        return pet

    def ask_question(self, question):
        """
        use for asking question
        :param question: gameplay question
        :return: user response to question
        """
        response = input(question)
        return response
