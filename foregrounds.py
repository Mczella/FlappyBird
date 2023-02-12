import pyglet
from random import randrange
from images import pipes


class Foreground:
    def __init__(self, window):
        self.speed_x = 120
        self.speed_y = 0
        self.batch = pyglet.graphics.Batch()
        self.foreground = [
            pyglet.sprite.Sprite(pipes, x=window.width / 3 + window.width, y=window.height / 2 + randrange(-90, 90),
                                 batch=self.batch),
            pyglet.sprite.Sprite(pipes, x=window.width / 3 * 2 + window.width, y=window.height / 2 + randrange(-90, 90),
                                 batch=self.batch),
            pyglet.sprite.Sprite(pipes, x=window.width / 3 * 3 + window.width, y=window.height / 2 + randrange(-90, 90),
                                 batch=self.batch)
        ]
        self.window = window

    def tik(self, dt):
        self.foreground[0].x -= self.speed_x * dt
        self.foreground[1].x -= self.speed_x * dt
        self.foreground[2].x -= self.speed_x * dt

        if self.foreground[0].x <= -self.foreground[0].width:
            self.foreground[0].x = self.window.width + self.foreground[0].width / 2
            self.foreground[0].y = self.window.height / 2 + randrange(-90, 90)
        if self.foreground[1].x <= -self.foreground[1].width:
            self.foreground[1].x = self.window.width + self.foreground[0].width / 2
            self.foreground[1].y = self.window.height / 2 + randrange(-90, 90)
        if self.foreground[2].x <= -self.foreground[2].width:
            self.foreground[2].x = self.window.width + self.foreground[0].width / 2
            self.foreground[2].y = self.window.height / 2 + randrange(-90, 90)
