# class Character():
#     def __init__(self):
#         self.name =""
#         self.status = ""
#         self.strength = 0
#         self.midi_count = 0
#         self.home = ""
#
#     def fight(self):
#         print("Lightsaber on! " + self.name)
#
# jedi_1 = Character()
#
# jedi_1.name = "Yoda"
# jedi_1.status = "Jedi Master"
# jedi_1.strength = 100
# jedi_1.midi_count = 20
# jedi_1.home = "Unknown"
#
# jedi_2 = Character()
#
# jedi_2.name = "Obi Wan Kenobi"
# jedi_2.status = "Jedi Master"
# jedi_2.strength = 65
# jedi_2.midi_count = 10
# jedi_2.home = "IDK"
#
#
# sithlord_1 = Character()
#
# sithlord_1.name = "Darth Vader"
# sithlord_1.status = "Sith Lord"
# sithlord_1.strength = 85
# sithlord_1.midi_count = 15
# sithlord_1.home = "Tatooine"
#
# print("The first object created was " + jedi_1.name)
# print("The second object created was " + jedi_2.name)
# sithlord_1.fight()

class Character():
    def __init__(self,name):
        self.name = name

    def fight(self):
        print("Lightsaber on! " + self.name)

class Droid(Character):
    def beep(self):
        print("BEEP! " + self.name)

class Jedi(Character):
    def __init__(self,name,status,strength,midi_count,home):
        super().__init__(name)
        self.status = status
        self.strength = strength
        self.midi_count = midi_count
        self.home = home

    def fight(self):
        super().fight()
        print("Lightsaber on! Jedi " + self.name)

class Sith(Character):
    def __init__(self,name,status,strength,midi_count,home):
        super().__init__(name)
        self.status = status
        self.strength = strength
        self.midi_count = midi_count
        self.home = home

    def fight(self):
        print("Lightsaber on! Sith " + self.name)

# jedi = Character("Luke Skywalker","Jedi Master",110,200,"Tatooine")
# jedi.fight()

droid = Droid("R2D2")
droid.beep()