import arcade
import random
"""
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be randomly placed somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
"""
arcade.open_window(500, 300, "1000 Circles")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()


class Circle():
    def __init__(self, x, y, radius, r, g, b):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 300)
        self.radius = 10
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def draw_circle(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, (self.r, self.g, self.b))


def main():
    for i in range(10000):
        circle = Circle(random.randint(0, 500), random.randint(0, 300), 10, random.randint(0, 255),
                        random.randint(0, 255), random.randint(0, 255))
        circle.draw_circle()


if __name__ == "__main__":
    main()

arcade.finish_render()
arcade.run()
