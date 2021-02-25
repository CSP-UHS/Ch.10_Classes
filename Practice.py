class Character:
    def __init__(self,name,status,strenght,mc,home):
        self.name=name
        self.status=status
        self.strength=strenght
        self.midichlorian_count=0
        self.home=home

    def fight(self):
        print("Lightsaber activated!, says ", self.name)

jedi_1 = Character("Obi-Wan Kenobi","Jedi Master","100",20,"Tatooine")


class Droid(Character):
    def beep(self):
        print("Beep, Beep says", self.name)
    def fight(self):
        super().fight()
        print("I'm stunning you!, says" , self.name)


object1 = Droid("R2D2","robot",2,0,"Tatooine")

object1.beep()
object1.fight()

