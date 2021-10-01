import numpy as np
import pygame, sys
from pygame.locals import *
BLACK  = (0, 0,0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE   = (0,0,255)
GREEN = (0,255,0)

class Cors:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Square:
    def __init__(self,x,y,cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size


def slope_intercept(x1,x2,y1,y2):
    L = []
    x = x1
    y = y1
    dx = x2-x1
    dy = y2-y1
    m = dy/dx
    b = y1 - m *x1
    while(x<=x2):
        L.append(Cors(x,y))
        x = x+1
        y = round(m*x+b)
    return L


def draw_squares(surface,width,height,cell_size):
    #rects = np.zeros((int(width/cell_size),int(height/cell_size)))
    squares = []
    i = 0;
    for x in range(0,int(width),cell_size):
        j = 0;
        for y in range (0,int(height),cell_size):
            squares.append(Square(x,y,cell_size))
            pygame.draw.rect(surface,BLACK,pygame.Rect((x,y),(cell_size,cell_size)),1)
            j = j + 1
        i = i + 1
    return squares 

def draw_square(surface, square,color):
    pygame.draw.rect(surface,color,pygame.Rect((square.x,square.y),(square.cell_size,square.cell_size)),0)
    return True

def draw_at_pos(surface,squares,x,y,color):
    for square in squares:
        if (square.x <= x and (square.x + square.cell_size) > x):
            if (square.y <= y and (square.y + square.cell_size) > y):
                draw_square(surface,square,color)
    return True

def draw_at_positions(surface,squares,L,color):
    for cors in L:
        draw_at_pos(surface,squares,cors.x,cors.y,color)
    return True
pygame.init()
# Create the window, saving it to a variable.
surface = pygame.display.set_mode((350, 250), pygame.RESIZABLE)
pygame.display.set_caption("Example resizable window")

while True:
    surface.fill((255,255,255))
    height = surface.get_height()
    width = surface.get_width()
    cell_size = 20
    point1 = width/2, height
    point2 = width/2, 0
    lineWidth = surface.get_width()/100
    # Draw a red rectangle that resizes with the window.
    squares = draw_squares(surface,width/2,height,cell_size)
    L = slope_intercept(0,width/2,height,0)
    draw_at_positions(surface,squares,L,BLUE)
    NumberOfCellsPerLine = 20
    

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)



     