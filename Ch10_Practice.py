class Character():  # Capitalize the first letter of the class
    def __init__(self):  # can change "self" into anything, but it's not needed ; AKA: constructor
        self.name = ""
        self.status = ""
        self.strength = 0
        self.midichlorian_count = 0
        self. home = ""

    def fight(self):
        print()
        print("Lightsaber on!, says " + self.name + ".")


jedi_1 = Character()
jedi_1.name = "yoda"
jedi_1.status = "Jedi Master"
jedi_1.strength = 100
jedi_1.midichlorian_count = 20
jedi_1.home = "Dagobah"
# =============================
jedi_2 = Character()
jedi_2.name = "Obi-Wan Kenobi"
jedi_2.status = "Jedi Master"
jedi_2.strength = 50
jedi_2.midichlorian_count = 10
jedi_2.home = "Stewjon"
# =============================
sithlord_1 = Character()
sithlord_1.name = "Darth Vader"
sithlord_1.fight()
# =============================
print("The first object created was " + jedi_1.name + ".")
print("The second object created was " + jedi_2.name + ".")
print("=============================")
# =============================


class Character():
    def __init__(self, name, status, strength, mc, home):
        self.name = name
        self.status = status
        self.strength = strength
        self.mc = mc
        self. home = home

    def fight(self):
        print("Lightsaber on!, says " + self.name + ".")


jedi = Character("Luke Skywalker", "Jedi Knight", 100, 200, "Tatooine")
jedi.fight()
print("=============================")
# =============================


class Character():
    def __init__(self, name):
        self.name = name

    def fight(self):
        print("Lightsaber on!, says " + self.name + ".")


class Droid(Character):
    def beep(self):
        print("Beep!, says " + self.name + ".")


droid = Droid("R2D2")
droid.beep()
print("=============================")
# =============================



class Character():
    def __init__(self, name):
        self.name = name

    def fight(self):
        print("Lightsaber on!, says " + self.name + ".")


class Jedi(Character):
    def __init__(self, name, strength):  # this init overrides the Character's init
        self.strength = strength
        super().__init__(name)

    def fight(self):
        super().fight()
        print("Come to the Light Side! My strength is", self.strength)
        print("=============================")



class Sith(Character):
    def __init__(self, name, myApprentice):
        self.myApprentice = myApprentice
        super().__init__(name)

    def fight(self):
        super().fight()
        print("Come to the Dark Side!, says " + self.name + ".")
        print("My apprentice is " + self.myApprentice + ".")
        print("=============================")


luke = Jedi("Luke Skywalker", 100)
vader = Sith("Darth Sideous", "Darth Vader")
luke.fight()
vader.fight()
# =============================
