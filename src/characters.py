import copy

import pyglet
from collision import is_collision
from images import birdImage, dead


class Character:
    def __init__(self, window, fg, bg):
        self.speed_x = 0
        self.speed_y = -100
        self.window = window
        self.character = pyglet.sprite.Sprite(birdImage, x=self.window.width / 3, y=self.window.height / 2)
        self.dead = False
        self.fg = fg
        self.bg = bg
        self.counter_clock = 0
        self.best_count = 0

        window.push_handlers(on_key_press=self.jump)
        window.push_handlers(on_key_press=self.reset)

    def tik(self, dt):
        self.character.x += self.speed_x * dt
        self.character.y += self.speed_y * dt

        if is_collision(self.character, self.fg.foreground[0]) \
                or is_collision(self.character, self.fg.foreground[1]) \
                or is_collision(self.character, self.fg.foreground[2]):
            self.character.image = dead
            self.dead = True
            self.bg.speed_x = 0
            self.fg.speed_x = 0
            self.speed_y = -30
            if self.counter_clock > self.best_count:
                self.best_count = copy.copy(self.counter_clock)

    def counter(self, dt):
        if self.dead:
            return

        self.counter_clock = self.counter_clock + dt * 10

    def jump(self, key, mod):
        if self.dead:
            return

        if key == pyglet.window.key.SPACE:
            self.character.y += 50

    def reset(self, key, mod):
        if key == pyglet.window.key.ENTER:
            self.dead = False
            self.character.image = birdImage
            self.fg.foreground[0].x = self.window.width / 3 + self.window.width
            self.fg.foreground[1].x = self.window.width / 3 * 2 + self.window.width
            self.fg.foreground[2].x = self.window.width / 3 * 3 + self.window.width
            self.character.x = self.window.width / 3
            self.character.y = self.window.height / 2
            self.bg.speed_x = 68
            self.fg.speed_x = 120
            self.speed_y = -100
            self.counter_clock = 0
