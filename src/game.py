import pyglet
from characters import Character
from foregrounds import Foreground
from backgrounds import Background
from collision import is_collision
from distance_of_points import distance
from labels import make_game_over_label, make_play_again_label, make_start_label


class Game():
    def __init__(self, window):
        self.fg = Foreground(window)
        self.bg = Background(window)
        self.bird = Character(window, self.fg, self.bg)
        self.window = window

        self.window.push_handlers(on_key_press=self.start)
        self.window.push_handlers(on_draw=self.draw)

        self.counter_label = None
        self.final_label = None
        self.started = False

    def start(self, key, mod):
        if not self.started and key == pyglet.window.key.SPACE:
            pyglet.clock.schedule_interval(self.bird.tik, 1 / 25)
            pyglet.clock.schedule_interval(self.bird.counter, 1 / 25)
            pyglet.clock.schedule_interval(self.fg.tik, 1 / 25)
            pyglet.clock.schedule_interval(self.bg.tik, 1 / 25)
            self.window.remove_handler("on_key_press", self.start)
            self.started = True

    def draw(self):
        self.window.clear()
        self.bg.batch.draw()
        self.fg.batch.draw()
        self.bird.character.draw()
        if self.bird.counter_clock == 0:
            make_start_label(self.window).draw()
        self.counter_label = pyglet.text.Label(
            str(round(self.bird.counter_clock)),
            font_name="Helvetica",
            font_size=30,
            bold=True,
            color=(0, 0, 0, 255),
            x=self.window.width - 50,
            y=self.window.height - 50,
            anchor_x="center")
        self.counter_label.draw()
        self.final_label = pyglet.text.Label(f"Your best score is {round(self.bird.best_count)}.",
                                             font_name="Helvetica",
                                             font_size=18,
                                             bold=True,
                                             color=(0, 0, 0, 255),
                                             x=make_play_again_label(self.window).x,
                                             y=make_play_again_label(self.window).y - 30,
                                             anchor_x="center")
        if self.bird.dead:
            make_game_over_label(self.window).draw()
            make_play_again_label(self.window).draw()
            self.final_label.draw()
