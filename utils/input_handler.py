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
        for symbol in self.keys:
            if symbol == key.W:
                self.player.move_forward()
            elif symbol == key.A:
                self.player.turn_left()
            elif symbol == key.S:
                self.player.move_backward()
            elif symbol == key.D:
                self.player.turn_right()
