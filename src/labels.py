import pyglet


def make_start_label(window):
    return pyglet.text.Label(
        "PRESS SPACEBAR TO START JUMPING",
        font_name="Helvetica",
        font_size=20,
        bold=True,
        color=(0, 0, 0, 255),
        x=window.width / 2,
        y=window.height / 4,
        anchor_x="center")


def make_game_over_label(window):
    game_over_label = pyglet.text.Label(
        "GAME OVER",
        font_name="Helvetica",
        font_size=50,
        bold=True,
        color=(0, 0, 0, 255),
        x=window.width / 2,
        y=window.height / 2,
        anchor_x="center")
    return game_over_label


def make_play_again_label(window):
    play_again_label = pyglet.text.Label(
        "PRESS ENTER TO PLAY AGAIN",
        font_name="Helvetica",
        font_size=18,
        bold=True,
        color=(0, 0, 0, 255),
        x=window.width / 2,
        y=window.height / 3,
        anchor_x="center")
    return play_again_label
