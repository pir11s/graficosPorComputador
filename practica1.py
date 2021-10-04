import numpy as np
import pygame, sys
import math
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

class Button:
    def __init__(self,surface,pos,width,height,text):
        self.surface = surface
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        
    def isClicked(self,pos):
        if (self.pos.x <= pos.x and (self.pos.x + self.width) > pos.x):
            if (self.pos.y <= pos.y and (self.pos.y + self.height) > pos.y):
                return True
        return False

    def draw(self,color):
        pygame.draw.rect(self.surface,color,pygame.Rect((self.pos.x,self.pos.y),(self.width,self.height)),1)
        textsurface = self.font.render(self.text, False, (0, 0, 0))
        surface.blit(textsurface,(self.pos.x  + 5,self.pos.y))

class Square:
    def __init__(self,x,y,cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size


def slope_intercept(x1,y1,x2,y2):
    L = []
    if x2<x1:
        x1,y1,x2,y2 = x2,y2,x1,y1
    x = x1
    y = y1
    dx = x2-x1
    dy = y2-y1
    if dx != 0:
        if (dy/dx)>1:
            x,y = y,x
            m = 1 / (dy/dx)
        else:
            m = dy/dx
    b = y1 - m *x1
    while(x<=x2):
        if y1 == y2:
            L.append(Cors(x,y1))
        if x1 == x2:
            L.append(Cors(x1,y))
        else:
            L.append(Cors(x,y))
            y = round(m*x+b)
        x = x+1
    return L

def digital_differential_analyzer(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    m =   max([abs(dx),abs(dy)])  
    dx2 = dx / m
    dy2 = dy / m
    x = x1 + 0.5
    y = y1 + 0.5
    i = 0
    L = []
    while i < m:
        L.append(Cors(math.floor(x),math.floor(y)))
        x = x + dx2
        y = y + dy2
        i = i + 1
    return L

def bresenham(x1,y1,x2,y2):
    if x2<x1:
        x1,y1,x2,y2 = x2,y2,x1,y1
    x = x1
    y = y1
    dx = abs(x2-y1)
    dy = abs(y2-y1)
    if dx != 0:
        if (dy/dx)>1:
            x,y = y,x
            m = 1 / (dy/dx)
        else:
            m = dy/dx
    ne = 2 * dy - dx
    L = []
    i = 0
    while i < dx:
        if y1 == y2:
            L.append(Cors(x,y1))
        if x1 == x2:
            L.append(Cors(x1,y))
        else:
            L.append(Cors(x,y))
        while ne > 0:
            y = y + 1
            ne = ne - 2 * dx
        x = x + 1
        e = ne + 2 * dy
        i = i + 1 

def draw_pixels(surface,L,color):
    for cors in L:
        surface.set_at((cors.x, cors.y), color)
    return True

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
surface = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
pygame.display.set_caption("Practica 1")
selectedAlgorithm = "Slope intercept"
while True:
    surface.fill((255,255,255))
    height = surface.get_height()
    width = surface.get_width()
    cell_size = 10
    point1 = width/2, height
    point2 = width/2, 0
    lineWidth = surface.get_width()/100

    L = []
    # Draw a red rectangle that resizes with the window.
    squares = draw_squares(surface,width/2,height,cell_size)
    
    
    NumberOfCellsPerLine = 20

    selectedPoints = []
    
    Buttons = [
        Button(surface,Cors(width / 2 + 25,height * 1 / 5),180,30,"Slope intercept"),
        Button(surface,Cors(width / 2 + 25,height * 2 / 5),180,30,"Digital Analyzer"),
        Button(surface,Cors(width / 2 + 25,height * 3 / 5),180,30,"Bresenham")
    ]
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            cors = Cors(x,y)
    

    if (cors.x < width / 2):
        selectedPoints.append(cors)

    if (len(selectedPoints) == 2):
        if selectedAlgorithm == "Slope Intercept":
            L = slope_intercept(selectedPoints[0].x,selectedPoints[0].y,selectedPoints[1].x,selectedPoints[1].y)
        if selectedAlgorithm == "Digital Analyzer":
            L = digital_differential_analyzer(selectedPoints[0].x,selectedPoints[0].y,selectedPoints[1].x,selectedPoints[1].y)
        if selectedAlgorithm == "Bresenham":
            L = bresenham(selectedPoints[0].x,selectedPoints[0].y,selectedPoints[1].x,selectedPoints[1].y)
        draw_at_positions(surface,squares,L,BLACK)
        selectedPoints = []
        L = []
    for button in Buttons:
        if button.isClicked(cors):
            selectedAlgorithm = button.text
        if selectedAlgorithm == button.text:
            button.draw(GREEN)
        else:
            button.draw(BLACK)

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
            width, height = event.size
            if width < 1000:
                width = 1000
            if height < 600:
                height = 600
            screen = pygame.display.set_mode((width,height), HWSURFACE|DOUBLEBUF|RESIZABLE)



    