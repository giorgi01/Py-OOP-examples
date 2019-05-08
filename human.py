import random


class Human:

    def __init__(self, firstname, lastname, age, gender):
        self.name = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.hunger = 80  # Max = 100
        self.energy = 0  # Max = 100

    def hi(self):
        print(f'Hi, I am {self.name}')

    def eat(self, food, calories):
        self.hunger -= calories * 0.2
        print(f'{self.name} ate {food}')
        print(f'Hunger level: {self.hunger}')

    def sleep(self, hours):
        self.energy += hours * 12
        print(f'{self.name} awoke after {hours} hours sleep')
        print(f'Energy level: {self.energy}')

    def do_something(self):
        print(f'{self.name} did something')
        self.energy -= random.randrange(1, 40)
        self.hunger += random.randrange(1, 40)
        print(f'Hunger level: {self.hunger}')
        print(f'Energy level : {self.energy}')


jason = Human('Jason', 'White', 22, 'Male')
jason.hi()
jason.eat('Hot-dog', 200)
jason.sleep(6)
jason.do_something()
