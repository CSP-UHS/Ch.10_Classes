class Character():
    def __int__(self):
        self.name = ""
        self.status = ""
        self.strength = 0
        self.midichlorian_count = 0
        self.home = ""
    def fight(self):
        print("Hi")
jedi_1 = Character()
jedi_1.name ="Alex"
jedi_1.status = "Initiate"
jedi_1.strength = 50
jedi_1.midichlorian_count = 20
jedi_1.home = "Urbandale"

jedi_1.fight()