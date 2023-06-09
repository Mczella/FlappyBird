from pyglet.gl import *
from game import Game

window = pyglet.window.Window(width=680, height=452)
pyglet.gl.glClearColor(114, 159, 207, 100)

game = Game(window)

pyglet.app.run()
