import pyglet

pipes = pyglet.image.load("pipes2.png")
pipes.anchor_x = pipes.width // 2
pipes.anchor_y = pipes.height // 2
birdImage = pyglet.image.load("bird.png")
birdImage.anchor_x = birdImage.width // 2
birdImage.anchor_y = birdImage.height // 2
sky = pyglet.image.load("sky.png")
dead = pyglet.image.load("dead.png")
dead.anchor_x = dead.width // 2
dead.anchor_y = dead.height // 2
