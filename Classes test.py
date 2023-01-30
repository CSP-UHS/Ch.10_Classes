# class Character():
#     def __init__(self):
#         self.name = ""
#         self.status = ""
#         self.strength = 0
#         self.midichlorian_count = 0
#         self.home = ""
# # Create a Character
# jedi_1 = Character()
# jedi_1.name = "Obi Wan Kenobi"
# jedi_1.status = "Jedi Master"
# jedi_1.strength = 100
# jedi_1.midichlorian_count = 20
# jedi_1.home = "Tatooine"
#
# jedi_2 = Character()
# jedi_2.name = "Yoda"
# jedi_2.status = "Jedi Master"
# jedi_2.strength = 200
# jedi_2.midichlorian_count = 50
# jedi_2.home = "Dagobah"
#
# print("The first object created was "+jedi_1.name)
# print("The second object created was "+jedi_2.name)


class Character():
    def __init__(self,new_name):
        self.name = new_name

    def fight(self):
        print("Lightsaber on!, says "+self.name)


class Jedi(Character):
    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength
    def fight(self):
        print("Lightsaber on!, says " + self.name)

class Droid(Character):
    def beep(self):
        print("Beep, says "+self.name)

droid = Droid("R2D2")
droid.beep()

jedi = Jedi("Luke Skywalker",100)
jedi.fight()