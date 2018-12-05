from pet import Tamagochi


class Cat(Tamagochi):
    def __init__(self):
        Tamagochi.__init__(self,'Cat')
    def __str__(self):
        return self.name

class Dog(Tamagochi):
    def __init__(self):
        Tamagochi.__init__(self,'Dog')
    def __str__(self):
        return self.name

class Rabbit(Tamagochi):
    def __init__(self):
        Tamagochi.__init__(self,'Rabbit')
    def __str__(self):
        return self.name

class Bird(Tamagochi):
    def __init__(self):
        Tamagochi.__init__(self,'Bird')
    def __str__(self):
        return self.name

class Dragon(Tamagochi):
    def __init__(self):
        Tamagochi.__init__(self,'Dragon')
    def __str__(self):
        return self.name

