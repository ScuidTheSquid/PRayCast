from pyglet.window import key

class InputHandler:
    def __init__(self, player):
        self.player = player
        self.keys = set()

    def on_key_press(self, symbol, modifiers):
        self.keys.add(symbol)

    def on_key_release(self, symbol, modifiers):
        self.keys.discard(symbol)

    def update(self, dt):
        if key.W in self.keys:
            self.player.move_forward(dt)
        if key.A in self.keys:
            self.player.turn_left(dt)
        if key.S in self.keys:
            self.player.move_backward(dt)
        if key.D in self.keys:
            self.player.turn_right(dt)