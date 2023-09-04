import math
import pyglet
from pyglet.shapes import Line, Circle
from utils.collision import is_collision
from assets.maps import map

class Player:
    def __init__(self, x, y, a, map):
        self.x = x
        self.y = y
        self.angle = a
        self.fov = 70
        self.map = map
        self.turnMultiplier = 50
        self.speed = 50
        self.radius = 5  # Radius of the player's circle
        self.grid_size = 32  # Assuming each grid cell is 32x32 pixels
        
    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Check if the proposed new position has a collision
        if not is_collision(new_x, new_y, self.map, self.grid_size):
            self.x, self.y = new_x, new_y
        else:
            # Calculate a slide vector based on the angle
            slide_x = dx
            slide_y = dy
            
            angle_deg = math.degrees(math.atan2(dy, dx))
            # Calculate the direction the player is trying to move
            if -45 < angle_deg <= 45:
                slide_x = dx
                slide_y = 0
            elif 45 < angle_deg <= 135:
                slide_x = 0
                slide_y = dy
            elif -135 < angle_deg <= -45:
                slide_x = 0
                slide_y = dy
            else:
                slide_x = dx
                slide_y = 0
            
            # Attempt to apply the slide vector
            new_x = self.x + slide_x
            new_y = self.y + slide_y
            
            if not is_collision(new_x, new_y, self.map, self.grid_size):
                self.x, self.y = new_x, new_y

    def move_forward(self, dt):
        distance = self.speed * dt
        dx = math.sin(self.angle * math.pi / 180) * distance
        dy = math.cos(self.angle * math.pi / 180) * distance
        self.move(dx, dy)

    def move_backward(self, dt):
        distance = -self.speed * dt
        dx = math.sin(self.angle * math.pi / 180) * distance
        dy = math.cos(self.angle * math.pi / 180) * distance
        self.move(dx, dy)

    def turn_left(self, dt):
        self.angle -= self.turnMultiplier * dt

    def turn_right(self, dt):
        self.angle += self.turnMultiplier * dt

    def update(self):
        # The update function can be empty or contain additional logic if needed
        pass

    def draw(self):
        # Draw the player as a line (representing player's direction)
        plx = self.x + math.sin(self.angle * math.pi / 180) * 100
        ply = self.y + math.cos(self.angle * math.pi / 180) * 100
        player_line = Line(self.x, self.y, plx, ply, width=2, color=(0, 0, 255))

        # Draw a circle around the player to represent the player's position and collision radius
        circle = Circle(x=self.x, y=self.y, radius=self.radius, color=(50, 225, 30))

        # Draw both the line and the circle
        player_line.draw()
        circle.draw()
