"""
Sign your name: Joe Schmidt
 
 1. Write code that defines a class named Animal:
     * Add a constructor for the Animal class that prints 'An animal has been born.'
     * Add an attribute for the animal name.
     * Add an eat() method for Animal that prints 'Munch munch.'
     * Add a make_noise() method for Animal that prints 'Grrr says [animal name].'

     
 2. Write code that defines a class named Cat:
     * Make Animal the parent.
     * Add a constructor for Cat that prints 'A cat has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Cat that prints 'Meow says [animal name].'

     
 3. Write code that defines a class named Dog:
     
     * Make Animal the parent.
     * Add a constructor for Dog that prints 'A dog has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Dog that prints 'Bark says [animal name].'

     
 4. Write a main program with:
     
     * Code that creates a cat, two dogs, and an animal with names.
     * Code that calls eat() and make_noise() for each animal.
     
 OUTPUT:
An animal has been born.
A cat has been born.
Munch munch
Meow says (cat name) .
An animal has been born.
A dog has been born.
Munch munch
Bark says (dog name).
An animal has been born.
A dog has been born.
Munch munch
Bark says (another dog name) .
An animal has been born.
Munch munch
Grrr says (animal name) .
"""


# class Character:
#     def __init__(self, name, strength, magic, agility, race, kingdom):
#         self.name = name
#         self.strength = strength
#         self.magic = magic
#         self.agility = agility
#         self.race = race
#         self.kingdom = kingdom
#
#     def combat(self):
#         print(self.name + ", what would you like to do?")
#         print()
#
#
# class NPC(Character):
#     def __init__(self, name, age, strength, magic, agility, race, kingdom):
#         super().__init__(name, strength, magic, agility, race, kingdom)
#         # self.name = name
#         self.age = age
#         # self.race = race
#         # self.kingdom = kingdom
#
#     def introduction(self):
#         print("My name is", self.name + ". I hale from", self.kingdom + ".")
#
#     def combat(self):
#         # super().combat()
#         super(NPC, self).combat()
#         print("\"I'm not cut out for this!\", says", self.name + ".")
#
#
# player_1 = Character("Erion", 10, 5, 5, "Drow", "Orelion")
#
# player_2 = Character("Argon", 5, 10, 5, "Human", "Lirenor")
#
# player_3 = Character("Mira", 5, 5, 10, "Wood elf", "Grendilum")
#
# npc_1 = NPC("Harold", 46, 1, 1, 3, "Halfling", "Hillshire")
#
# # player_1.name = "Erion"
# # player_1.power = 10
# # player_1.magic = 5
# # player_1.race = "Drow"
# # player_1.kingdom = "Orelion"
#
# print(player_1.name, player_1.race, player_1.kingdom)
# print()
#
# player_1.combat()
# player_2.combat()
# player_3.combat()
#
# npc_1.introduction()
# npc_1.combat()
# print(npc_1.age)

class Animal:
    def __init__(self, name):
        print("An animal has been born.")
        self.name = name

    def eat(self):
        print("Munch munch")

    def make_noise(self):
        print("Grrr says", self.name + ".")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A cat has been born.")

    def eat(self):
        super().eat()

    def make_noise(self):
        print("Moew says", self.name + ".")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A dog has been born.")

    def eat(self):
        super().eat()

    def make_noise(self):
        print("Bark, says", self.name + ".")


def main():
    cat_1 = Cat("Herb")
    cat_1.eat()
    cat_1.make_noise()
    dog_1 = Dog("Sparky")
    dog_1.eat()
    dog_1.make_noise()
    dog_2 = Dog("Blitz")
    dog_2.eat()
    dog_2.make_noise()
    nonbinary_1 = Animal("Fritz")
    nonbinary_1.eat()
    nonbinary_1.make_noise()


if __name__ == "__main__":
    main()
