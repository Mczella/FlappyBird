import pyglet
from images import sky


class Background:
    def __init__(self, window):
        self.speed_x = 68
        self.speed_y = 0
        self.batch = pyglet.graphics.Batch()
        self.background = [
            pyglet.sprite.Sprite(sky, x=0, y=0, batch=self.batch),
            pyglet.sprite.Sprite(sky, x=680, y=0, batch=self.batch)
        ]

    def tik(self, dt):
        self.background[0].x -= self.speed_x * dt
        if self.background[0].x <= -self.background[0].width:
            self.background[0].x = 0
        self.background[1].x = self.background[0].x + self.background[0].width
