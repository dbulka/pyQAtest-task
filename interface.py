from pet import Tamagochi


class Showable:

    def show_tamagochi(self, pet):
        """показывает характеристики питомца"""
        print('hp: {0}| hunger: {1} | happines: {2} | alive: {3}'.format(pet.hp, pet.hunger, pet.happiness, pet.alive))

    def show_game_result(self,n,alive):
        """показывает результат игры"""
        print('%s on %s th step' % ('YOU WIN!' if (alive and n > 100) else 'YOU LOSE!', n))

    def ask_question(self, question):
        """задаёт вопрос"""
        response = input(question)
        return response

    def choose_pet(self):
        """содержит список питомцев"""
        pets = ['cat', 'dog', 'bird']
        return pets



