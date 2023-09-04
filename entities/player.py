import math
import pyglet
from pyglet.shapes import Line, Circle
from utils.collision import is_collision

class Player:
    def __init__(self, x, y, a, map):
        self.x = x
        self.y = y
        self.angle = a
        self.map = map
        self.speed = 5
        self.radius = 5  # Radius of the player's circle

    def update(self):
        new_x = self.x + math.sin(self.angle * math.pi / 180) * self.speed
        new_y = self.y + math.cos(self.angle * math.pi / 180) * self.speed
        if not is_collision(new_x, new_y, self.map):
            self.x, self.y = new_x, new_y

    def draw(self):
        # Draw the player as a line (representing player's direction)
        plx = self.x + math.sin(self.angle * math.pi / 180) * 10
        ply = self.y + math.cos(self.angle * math.pi / 180) * 10
        player_line = Line(self.x, self.y, plx, ply, width=2, color=(255, 0, 0))

        # Draw a circle around the player to represent the player's position and collision radius
        circle = Circle(x=self.x, y=self.y, radius=self.radius, color=(50, 225, 30))

        # Draw both the line and the circle
        player_line.draw()
        circle.draw()
