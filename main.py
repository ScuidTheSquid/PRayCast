import pyglet
from entities.player import Player
from entities.box import Box
from assets.maps import map
from utils.input_handler import InputHandler

# Initialize Pyglet window
window = pyglet.window.Window(800, 600, "PRayCast")

# Initialize player, boxes, and input handler
player = Player(100, 500, 45, map)
boxes = [Box(j * 32, 600 - (i * 32) - 32, 32, 32) for i, row in enumerate(map) for j, cell in enumerate(row) if cell == 1]
input_handler = InputHandler(player)

@window.event
def on_draw():
    window.clear()
    player.draw()
    for box in boxes:
        box.draw()

pyglet.app.run()
