#main.py

import math
import time
import pyglet

px = 100
py = 100
pa = 45

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    pass


def drawPlayer(px, py, a):
    plx = px - math.sin(a*math.pi/180)*10
    ply = py - math.cos(a*math.pi/180)*10
    player = pyglet.shapes.Line(px, py, plx, ply)
    
    player.draw()

@window.event
def on_draw():
    window.clear()
    drawPlayer(px, py, pa)

pyglet.app.run()