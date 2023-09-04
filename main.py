import pyglet
from entities.player import Player
from entities.box import Box
from assets.maps import map
from utils.input_handler import InputHandler

# Initialize Pyglet window
window = pyglet.window.Window(800, 600, "PRayCast")

# Initialize player, boxes, and input handler
player = Player(115, 500, 45, map)
boxes = [Box(j * 32, 600 - (i * 32) - 32, 32, 32) for i, row in enumerate(map) for j, cell in enumerate(row) if cell == 1]
input_handler = InputHandler(player)

@window.event
def on_draw():
    window.clear()
    player.draw()
    for box in boxes:
        box.draw()

@window.event
def on_key_press(symbol, modifiers):
    input_handler.on_key_press(symbol, modifiers)

@window.event
def on_key_release(symbol, modifiers):
    input_handler.on_key_release(symbol, modifiers)

def update(dt):
    input_handler.update(dt)
    # Add any other game logic updates here

pyglet.clock.schedule_interval(update, 1 / 144.0)  # Set the update interval to 60 FPS

pyglet.app.run()
