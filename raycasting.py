import math
import pyglet

class Raycaster:
    def __init__(self, player, window):
        self.player = player
        self.window = window
        self.map = map
        self.num_rays = 10
        self.ray_length = 400

    def draw(self):
        ray_angle_increment = self.player.fov / self.num_rays
        half_fov = self.player.fov / 2
        start_angle = self.player.angle - half_fov + ray_angle_increment / 2

        for ray_num in range(self.num_rays):
            ray_angle = start_angle + ray_angle_increment * ray_num
            ray_x = self.player.x
            ray_y = self.player.y
            ray_dx = ray_x + math.sin(math.radians(ray_angle)) * self.ray_length
            ray_dy = ray_y + math.cos(math.radians(ray_angle)) * self.ray_length

            ray = pyglet.shapes.Line(ray_x, ray_y, ray_dx, ray_dy, color=(255, 0, 0))
            ray.draw()
