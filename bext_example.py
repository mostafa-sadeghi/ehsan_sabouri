import bext
import random
import time
import sys


WIDTH, HEIGHT = bext.size()
# print(WIDTH, HEIGHT)
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'megenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

bext.clear()
logos = []

for i in range(NUMBER_OF_LOGOS):
    logos.append({
        COLOR: random.choice(COLORS),
        X: random.randint(1, WIDTH - 3),
        Y: random.randint(1, HEIGHT - 3),
        DIR: random.choice(DIRECTIONS)
    })

cornerBounces = 0
while True:
    for logo in logos:
        bext.goto(logo[X], logo[Y])

        originalDirection = logo[DIR]

        if logo[X] == 0 and logo[Y] == 0:
            logo[DIR] = DOWN_RIGHT
            cornerBounces += 1
        elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
            logo[DIR] = UP_RIGHT
            cornerBounces += 1
        elif logo[X] == WIDTH - 3 and logo[Y] == 0:
            logo[DIR] = DOWN_LEFT
            cornerBounces += 1
        elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
            logo[DIR] = UP_RIGHT
            cornerBounces += 1

        elif logo[X] == 0 and logo[DIR] == UP_LEFT:
            logo[DIR] = UP_RIGHT
        elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
            logo[DIR] = DOWN_RIGHT

        elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
            logo[DIR] = UP_LEFT
        elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
            logo[DIR] = DOWN_LEFT

        elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
            logo[DIR] = DOWN_RIGHT
        elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
            logo[DIR] = DOWN_LEFT

        elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
            logo[DIR] = UP_RIGHT
        elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
            logo[DIR] = UP_LEFT

        if logo[DIR]
