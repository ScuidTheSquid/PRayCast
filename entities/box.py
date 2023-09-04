import pyglet

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
