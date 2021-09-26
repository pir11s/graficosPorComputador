import numpy as np
import pygame, sys
from pygame.locals import *
BLACK  = (0, 0,0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE   = (0,0,255)
GREEN = (0,255,0)
def draw_cells(surface,width,height,cell_size):
    #rects = np.zeros((int(width/cell_size),int(height/cell_size)))
    for i in range(0,int(width),cell_size):
        for j in range (0,int(height),cell_size):
            #rects[i][j] = pygame.Rect((i,j),(cell_size,cell_size))
            pygame.draw.rect(surface,BLACK,pygame.Rect((i,j),(cell_size,cell_size)),1)
    #return rects 


pygame.init()
# Create the window, saving it to a variable.
surface = pygame.display.set_mode((350, 250), pygame.RESIZABLE)
pygame.display.set_caption("Example resizable window")

while True:
    surface.fill((255,255,255))
    height = surface.get_height()
    width = surface.get_width()
    point1 = width/2, height
    point2 = width/2, 0
    lineWidth = surface.get_width()/100
    # Draw a red rectangle that resizes with the window.
    draw_cells(surface,width/2,height,20)
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



     