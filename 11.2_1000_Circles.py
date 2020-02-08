'''
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''
import arcade
import random

arcade.open_window(500, 300, "1000 Circles")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
########        Draw here
class circle():
    def __init__(self):
        self.x = random.randint(0,501)
        self.y = random.randint(0, 301)
        self.radius = 10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def draw_circle(self):
        for i in range(1000):
            arcade.draw_circle_filled(self.y, self.x, self.radius, self.color)

circle = circle()
circle.draw_circle()
######## Draw here
arcade.finish_render()
arcade.run()