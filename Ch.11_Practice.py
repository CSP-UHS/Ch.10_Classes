class Character:
    def __init__(self, name, status, strength, mc, home): # variables needed for character
        self.name = name
        self.status = status
        self.strength = strength
        self.midichlorian_count = mc
        self.home = home

    def fight(self):
        print("Lightsaber activate!, says", self.name) # says for any type of character when called


class Droid(Character):
    def __init__(self, name, status, strength, mc, home, type):
        super().__init__(name, status, strength, mc, home)
        self.type = type

    def beep(self):
        print("Beep, Beep, says", self.name) # will say this for a droid character when called

    def fight(self):
        super().fight()
        print("I'm stunning you!, says", self.name) # says for droid character when called


jedi_1 = Character("Obi-Wan Kenobi", "Jedi Master", 100, 20, "Tatooine") # makes character
jedi_1.fight()

jedi_2 = Character("Yoda", "Jedi Master", 200, 50, "Dagobah") # makes character
jedi_2.fight()

object_1 = Droid("R2D2", "Robot", 2, 0, "Naboo", "Class C Robot") # makes droid character
object_1.beep()
object_1.fight()