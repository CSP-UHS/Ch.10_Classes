'''
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be randomly placed somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''
import arcade
import random


class Circle():
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 300)
        self.r = 10
        self.c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_circle(self):

        arcade.draw_circle_filled(self.x,self.y,self.r,self.c)

def main():
    arcade.open_window(500, 300, "Circles")
    arcade.start_render()
    for i in range(1000):
        circle=Circle()
        circle.draw_circle()
    arcade.finish_render()
    arcade.run()



if __name__=="__main__":
    main()

