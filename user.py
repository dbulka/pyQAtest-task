from interface import Showable

class User(Showable):

    def give_food(self, pet):
        pet.hunger -= int(input('enter amount of food: '))

    def give_hp(self,cat):
        cat.hp  += int(input('enter amount of hp: '))

    def play(self,cat):
        cat.happiness  += int(input('enter amount of hp: '))

    def make_choice(self, n):
        print("""
        Make step:
        #1 - Feed pet
        #2 - Heal pet
        #3 - Play with pet
              """)
        condition = ('1','2','3')
        resp = True
        while resp:
            choice = self.ask_question('Enter number of step: ')
            if choice in condition:
                resp = False
            else:
                resp = True
                print('you entered wrong number')
        return choice



