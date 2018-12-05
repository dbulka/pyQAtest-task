from pet import random, Tamagochi
from user import User
from interface import Showable


class Gameplay:

    @staticmethod
    def step(pet):
        """
        change Tamagochi param
        :param pet: hp, happiness, hunger
        :return: changed Tamagochi hp, happiness, hunger
        """
        pet.hp -= random.randrange(5, 30)
        pet.happiness -= random.randrange(5, 30)
        pet.hunger += random.randrange(10, 50)

    def perfom_choice(self, pet, choice):
        """
        according to user make_choice choose way of changing Tamagochi param
        :param pet:
        :param choice: user make_choice
        :return: method, which will change chosen Tamagochi param
        """
        if choice is '1':
            do_user.give_food(pet)
        elif choice is '2':
            do_user.give_hp(pet)
        elif choice is '3':
            do_user.play(pet)

    def fifth_step(self, n, pet):
        """
        change Tamagochi hp every 5-th step
        :param n: step number
        :param pet: change Tamagochi hp
        """

        if n % 5 == 0:
            coin = random.randint(0, 1)
            print(coin, ' is coin')
            if coin == 0:
                pet.hp += random.randint(5, 50)
            else:
                pet.hp -= random.randint(5, 50)

    def main(self):
        """
        perfom gameplay
        :return: game result
        """

        # всё до game нужно добавить в main()?


        # создаём набор имён питомцев
        pets = game_interface.choose_pet()

        # выбираем имя питомца
        pet_name = pets[random.randrange(len(pets))]
        print('pet name - ',pet_name)

        #создаём питомца
        pet = Tamagochi(pet_name)

        # цикл выполняется пока n до 100 или alive = true
        n = 0
        while (pet.alive and n < 100):
            game_interface.show_tamagochi(pet)
            choice = do_user.make_choice(n)
            self.perfom_choice(pet, choice)
            n += 1
            self.fifth_step(n, pet)
            self.step(pet)
            pet.alive = pet.is_alive()
    # выводим результат игры
        game_interface.show_game_result(n, pet.alive)

# создаём класс интерфейса
game_interface = Showable()

#инициализация Юзера
do_user = User()

#закускаем код
game = Gameplay()
game.main()
