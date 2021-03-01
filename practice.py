class Character:
    def __init__(self, name, status, strength, mc, home):
        self.name = name
        self.status = status
        self.strength = strength
        self.midichlorian_count = mc
        self.home = home

    def fight(self):
        print("Lightsaber activate!, says ", self.name)


class Droid(Character):
    def __init__(self, name, status, strength, mc, home, typemodel):
        super().__init__(name, status, strength, mc, home)
        self.typemodel = typemodel

    def beep(self):
        print("Beep, Beep says ", self.name)

    def fight(self):
        print("I'm stunning you!, says", self.name)


object1 = Droid("R2D2", "Robot", 2, 0, "Tatooine", "robot")

object1.beep()

jedi_1 = Character("Obi-Wan Kenobi", "Jedi Master", 100, 20, "Tatooine")
jedi_1.fight()

# jedi_1.name = "Obi-Wan Kenobi"
# jedi_1.status = "Jedi Master"
# jedi_1.strength = "100"
# jedi_1.midichlorian_count = 20
# jedi_1.home = "Tatooine"


jedi_2 = Character("Yoda", "Jedi Master", 200, 50, "Dagobah")
jedi_2.fight()

# jedi_2.name = "Yoda"
# jedi_2.status = "Jedi Master"
# jedi_2.strength = "200"
# jedi_2.midichlorian_count = 50
# jedi_2.home = "Dagobah"
