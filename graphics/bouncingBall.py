# template code for you to fill in when making pygame program with moving pieces. no user controls
from random import randint

# dimensions of the window
width = 700
height = 500

circleY = 300
circleSpeedY = 15

squareX = 200
squareSpeedX = 10

r = 0
g = 255
b = 0

def move():
    global circleY, circleSpeedY, r, g, b

    circleY = circleY + circleSpeedY

    if circleY >= 450 or circleY <= 50:
        circleSpeedY = -1 * circleSpeedY
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)


def draw(canvas):
    canvas.fill((255,255,255))

    pygame.draw.circle(canvas, (r, g, b), (200,circleY), 50)


# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Graphics Starter')
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()

while True:
    move()
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)

















