class Boat():
    def __init__(self, name):
        self.name = name
        self.isDocked = True
    def dock(self):
        if self.isDocked == True:
            print(self.name,"is already docked")
        else:
            print(self.name, "is docking")
            self.isDocked = True
    def undock(self):
        if self.isDocked == False:
            print(self.name,"is already undocked")
        else:
            print(self.name,"is undocking")
            self.isDocked = False

class Submarine(Boat):
    def submerge(self):
        if self.isDocked == True:
            print(self.name,"can't submerge.")
        else:
            print(self.name,"is submerging")
            self.isDocked = True

def my_program():
    boat1 = Submarine("SS Georgie")
    boat1.dock()
    boat1.undock()
    boat1.undock()
    boat1.dock()
    boat1.dock()
    boat1.submerge()
    boat1.undock()
    boat1.submerge()

if __name__ == '__main__':
    my_program()

