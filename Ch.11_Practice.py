class Character:
    def __init__(self):
        self.name = ""
        self.status = ""
        self.strength = ""
        self.midichlorian_count = 0
        self.home = ""

jedi_1 = Character()


jedi_1.name = "Obi-Wan Kenobi"
jedi_1.status = "Jedi Master"
jedi_1.strength = "100"
jedi_1.midichlorian_count = 20
jedi_1.home = "Tatooine"

jedi_2 = Character()


jedi_2.name = "Yoda"
jedi_2.status = "Jedi Master"
jedi_2.strength = "200"
jedi_2.midichlorian_count = 50
jedi_2.home = "Dagobah"

print(jedi_1.name)
print(jedi_2.name)