class Boat:
    def __init__(self, name):
        self.name = name
        self.isDocked = True

    def dock(self):
        if self.isDocked is True:
            print(self.name, "is already docked.")
        else:
            print(self.name, "is docking.")
            self.isDocked = True

    def undock(self):
        if self.isDocked is False:
            print(self.name, "isn't docked.")
        else:
            print(self.name, "is undocking.")
            self.isDocked = False


class Submarine(Boat):
    def submerge(self):
        if self.isDocked is False:
            print(self.name, "is submerging!")
        else:
            print(self.name, "can't submerge!")


sub = Submarine("USS Hermon")
sub.dock()
sub.undock()
sub.undock()
sub.dock()
sub.dock()
sub.submerge()
sub.undock()
sub.submerge()
