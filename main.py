import pyglet
from entities.player import Player
from entities.box import Box
from assets.maps import map
from utils.input_handler import InputHandler
import raycasting

window = pyglet.window.Window(800, 600, "PRayCast")
player = Player(115, 500, 45, map)
boxes = [Box(j * 32, 600 - (i * 32) - 32, 32, 32) for i, row in enumerate(map) for j, cell in enumerate(row) if cell == 1]
input_handler = InputHandler(player)
raycaster = raycasting.Raycaster(player, window)

@window.event
def on_draw():
    window.clear()
    player.draw()
    
    for box in boxes:
        box.draw()
    raycaster.draw()
    

@window.event
def on_key_press(symbol, modifiers):
    input_handler.on_key_press(symbol, modifiers)

@window.event
def on_key_release(symbol, modifiers):
    input_handler.on_key_release(symbol, modifiers)

def update(dt):
    input_handler.update(dt)

pyglet.clock.schedule_interval(update, 1/30)
pyglet.app.run()
