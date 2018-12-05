from pet import Tamagochi


class Showable:

    def show_tamagochi(self, pet):
        """
        show Tamagochi state (param)
        :return: string with Tamagochi param
        """
        print('hp: {0}| hunger: {1} | happines: {2} | alive: {3}'.format(pet.hp, pet.hunger, pet.happiness, pet.alive))

    def show_game_result(self,n,alive):
        """
        show game result
        :param n: number of steps
        :param alive: state of Tamagochi alive
        :return: string with game result
        """
        print('%s on %s th step' % ('YOU WIN!' if (alive and n > 100) else 'YOU LOSE!', n))

    def ask_question(self, question):
        """
        use for asking question
        :param question: gameplay question
        :return: user response to question
        """
        response = input(question)
        return response

# переделать в отдельные классы
    def choose_pet(self):
        """содержит список питомцев"""
        pets = ['cat', 'dog', 'bird']
        return pets
