import math
import pyglet
from pyglet.window import key

px = 100
py = 500
pa = 45
player_speed = 5

map = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Flags to track key states
move_forward = False
move_backward = False
turn_left = False
turn_right = False

window = pyglet.window.Window(800, 600, "PRayCast")

@window.event
def on_key_press(symbol, modifiers):
    global pa, px, py, move_forward, move_backward, turn_left, turn_right
    if symbol == key.W:
        move_forward = True
    elif symbol == key.A:
        turn_left = True
    elif symbol == key.S:
        move_backward = True
    elif symbol == key.D:
        turn_right = True

@window.event
def on_key_release(symbol, modifiers):
    global move_forward, move_backward, turn_left, turn_right
    if symbol == key.W:
        move_forward = False
    elif symbol == key.A:
        turn_left = False
    elif symbol == key.S:
        move_backward = False
    elif symbol == key.D:
        turn_right = False

def update_player_position(dt):
    global pa, px, py
    if move_forward:
        new_px = px + math.sin(pa*math.pi/180) * player_speed
        new_py = py + math.cos(pa*math.pi/180) * player_speed
        if not is_collision(new_px, new_py):
            px, py = new_px, new_py
    if move_backward:
        new_px = px - math.sin(pa*math.pi/180) * player_speed
        new_py = py - math.cos(pa*math.pi/180) * player_speed
        if not is_collision(new_px, new_py):
            px, py = new_px, new_py
    if turn_left:
        pa -= 10
    if turn_right:
        pa += 10

pyglet.clock.schedule_interval(update_player_position, 1/60.0)

def draw_player(px, py, a):
    plx = px + math.sin(a*math.pi/180)*10
    ply = py + math.cos(a*math.pi/180)*10
    player = pyglet.shapes.Line(px, py, plx, ply, width=2, color=(255, 0, 0))

    # Draw a circle around the player with the same radius as collision detection
    radius = 5  # Adjust as needed
    circle = pyglet.shapes.Circle(x=px, y=py, radius=radius, color=(50, 225, 30))

    circle.draw()
    player.draw()

class Box:
    def __init__(self, x, y, width, height, borderColor=(255, 255, 255), color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.borderColor = borderColor

    def draw(self):
        box = pyglet.shapes.BorderedRectangle(self.x, self.y, self.width, self.height, border_color=self.borderColor, color=self.color)
        box.draw()

def draw_map():
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == 1:
                # Create a Box for walls (where map value is 1)
                box = Box(j * 32, 600 - (i * 32) - 32, 32, 32)  # Adjust position and size as needed
                box.draw()

def is_collision(new_px, new_py):
    # Check if the new player position collides with any walls
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == 1:
                box_x = j * 32
                box_y = 600 - (i * 32) - 32
                if (new_px + 5 >= box_x and new_px <= box_x + 32 and
                    new_py + 5 >= box_y and new_py <= box_y + 32):
                    return True
    return False

@window.event
def on_draw():
    window.clear()
    draw_map()
    draw_player(px, py, pa)

pyglet.app.run()
