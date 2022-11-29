
import sys
import pygame
from pygame.locals import KEYDOWN, K_q

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 1100, 1100
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
WHITE = (255, 255, 255)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 50, 50
# VARS:
_VARS = {'surf': False}


def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    _VARS['surf'].fill(WHITE)
    

    state = [[0,11,15,4], [0,0,15,11], [0, 0, 6, 11]]

    ScreenSize = 1000
    n = 15
    ratio = 1000 / n

    drawSquare(0, 0, n, n, ratio, n)

    
    for rec in state:
        drawSquare(rec[0], rec[1], rec[0] + rec[2], rec[1] + rec[3], ratio, n)


    while True:
        checkEvents()
        pygame.display.update()


def drawSquare(x1, y1, x2, y2, ratio, n):

    x1 = x1 * ratio
    x2 = x2 * ratio
    y1 = (n - y1) * ratio
    y2 = (n - y2) * ratio

    #draw bottum
    drawRect((x1, y1), (x2, y1))

    #draw right wall
    drawRect((x2, y1), (x2, y2))

    #draw top 
    drawRect((x2, y2), (x1, y2))

    #draw left wall
    drawRect((x1, y2), (x1, y1))



def drawRect(start, end):
    
    start

    pygame.draw.line(
      _VARS['surf'], BLACK,
      (start[0] + PADLEFTRIGHT, start[1] + PADTOPBOTTOM),
      (end[0] + PADLEFTRIGHT, end[1] + PADTOPBOTTOM), 3)
   


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
      



