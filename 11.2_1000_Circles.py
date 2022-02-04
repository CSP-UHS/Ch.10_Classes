import arcade
import random
radius = 10
graph_x = 500
graph_y = 300
class Circle():
    def __init__(self):
        self.x = random.randint(radius,graph_x-radius)
        self.y = random.randint(radius,graph_y-radius)
        self.radius = radius
        self.color1 = random.randint(0,255)
        self.color2 = random.randint(0, 255)
        self.color3 = random.randint(0, 255)
    def draw_circle(self):
        arcade.draw_circle_filled(self.x,self.y,self.radius,[self.color1, self.color2, self.color3])

def my_program():
    arcade.open_window(graph_x, graph_y, "1000 Circles", True)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    for i in range(1000):
        circle = Circle()
        circle.draw_circle()
    arcade.finish_render()
    arcade.run()
if __name__ == '__main__':
    my_program()
