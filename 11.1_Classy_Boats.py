'''
CLASSY BOATS
-----------------
Use the following Pseudocode to create this program:

1.) Create a class called Boat( )
2.) Use a constructor that sets two attributes: name and isDocked.
3.) The name should be entered as an argument when the object is created.
4.) The isDocked attribute is a Boolean variable. Set it to True.
5.) Add a method called dock( )
6.) In this method, if the boat is already docked print "(boat name) is already docked."
7.) If it is not docked, print "(boat name) is docking" and set the isDocked attribute to True.
8.) Add another method called un_dock( )
9.) In this method, if the boat is already un_docked print "(boat name) is already un_docked."
10.) If it is docked print "(boat name) is un_docking" and set the isDocked attribute to False.
11.) Add another class called Submarine( ) that will inherit the Boat( ) class.
12.) In the Submarine( ) class create a method called submerge( ) that will print "(boat name) is submerging" 
if the boat is un_docked and "(boat name) can't sumberge" if the boat is docked.
'''
isDocked = True


class Boat:
    def __init__(self, name, isDocked):
        self.name = name
        self.isDocked = True

    def dock(self):
        if self == isDocked:
            print(self.name, "is already docked")
        else:
            print(self.name, "is docking")
            self.isDocked = True

    def un_dock(self):
        if self == isDocked:
            print(self.name, "is now un_docking")
            self.isDocked = False
        else:
            print(self.name, "is already docked")
            self.isDocked = True


class Submarine(Boat):
    def __init__(self, name):
        self.name = name

    def submerge(self):
        if self.isDocked:
            print(self.name, "can'y submerge because it is docked!")
        else:
            print(self.name, "is now submerging!")


def main():
    sub = Submarine("USS GETZ")
    sub.dock()
    sub.un_dock()
    sub.un_dock()
    sub.dock()
    sub.dock()
    sub.submerge()
    sub.un_dock()
    sub.submerge()


if __name__ == "__main__":
    main()
'''
Let's Float the Boat
--------------------
13.) Instantiate an object of the Submarine( ) class. Don't forget to pass in a name.
14.) Call the dock( ) method once
15.) Call the un_dock( ) method twice
16.) Call the dock( ) method two more times
17.) Call the submerge( ) method once
18.) Call the un_dock( ) method once
19.) Call the submerge( ) method a final time.

OUTPUT:
USS Hermon is already docked.
USS Hermon is un_docking
USS Hermon is already un_docked.
USS Hermon is docking
USS Hermon is already docked.
USS Hermon can't submerge!
USS Hermon is un_docking
USS Hermon is submerging!
'''


