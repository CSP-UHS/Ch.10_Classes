# class Character():
#     def __init__(self,name,status,strength,mc,home):
#         self.name = ""
#         self.status= ""
#         self.strength = ""
#         self.mc = ""
#         self.home = ""
#
#     def fight(self):
#         print("Lightsaber on!, says " +self.name)
#
# jedi_1 = Character()
#
# jedi_1.name = "yoda"
# jedi_1.status = "Jedi Master"
# jedi_1.strength = "100"
# jedi_1.mc = 20
# jedi_1.home = "Dagobah"
#
# jedi_2 = Character()
# jedi_2.name = "Obi wan kenobi"
# jedi_2.status = "Jedi Master"
# jedi_2.strength = "50"
# jedi_2.mc = 10
# jedi_2.home = "Tatooine"
#
# sithlord_1 = Character()
# sithlord_1.name = "Darth Vader"
# sithlord_1.fight()
#
# print("The first object created was " + jedi_1.name)
# print("The second object created was " + jedi_2.name)

# ////////////////////////////////////////////////////////////////////////////////////////////
class Character():
    def __init__(self,name):
        self.name = name
    def fight(self):
        print("Lightsaber on!, says " +self.name)

class Jedi(Character):
    def __init__(self,name,strength):
        super().__init__(name)
        self.strength = strength
    def fight(self):
        super().fight()
        print("Come to the Light Side! My strength is " +self.strength)


class Sith(Character):
    def __init__(self,name,my_apprentice):
        super().__init__(name)
        self.my_apprentice = my_apprentice
    def fight(self):
        print("Come to the dark Side! says " +self.name)
        print("My apprentice is "+self.my_apprentice)

luke = Jedi("Luke Skywalker","100")
darth =Sith("Darth Sideous","Darth Vader")
luke.fight()
darth.fight()


# class Droid(Character):
#     def beep(self):
#         print("Beep, says "+self.name)

# droid = Droid("R2D2")
# droid.beep()

#
# jedi = Character("Luke Skywalker","Jedi Master",100,200,"Tatooine")
# jedi.fight()