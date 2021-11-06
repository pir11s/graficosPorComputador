import numpy as np
import pygame, sys
import math
from pygame.locals import *
BLACK  = (0, 0,0)
RED = (255,0,0)
BLUE   = (0,0,255)
GREEN = (0,255,0)

RED_TEXT = "Red"
BLUE_TEXT = "Blue"
GREEN_TEXT = "Green"
BLACK_TEXT = "Black"

BOARD_CELL_SIZE = 20

BOARD = "BOARD"
EMPTY = "EMPTY"

SLOPE_INTERCEPT = "Slope intercept"
DIGITAL_ANALYZER = "Digital Analyzer"
BRESENHAM = "Bresenham"
CLEAR = "Clear"

class Rect:
    def __init__(self,L,color):
        self.L = L
        self.color = color

class Cors:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Button:

    color = BLACK

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

    def activate(self):
        self.color = GREEN

    def desactivate(self):
        self.color = BLACK

    def draw(self):
        pygame.draw.rect(self.surface,self.color,pygame.Rect((self.pos.x,self.pos.y),(self.width,self.height)),1)
        textsurface = self.font.render(self.text, False, (0, 0, 0))
        surface.blit(textsurface,(self.pos.x  + 5,self.pos.y))

class Square:
    def __init__(self,x,y,cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size


def getColor(color):
    if color == RED:
        return RED
    if color ==BLUE:
        return BLUE
    if color == GREEN:
        return GREEN
    return BLACK


def activateButton(Buttons,name):
    for button in Buttons:
        if button.text == name:
            button.activate()
        else:
            button.desactivate()
    return ButtonsAlgorithms

def slope_intercept(x1,y1,x2,y2):
    L = []
    if x2<x1:
        x1,y1,x2,y2 = x2,y2,x1,y1
    x = x1
    y = y1
    dx = x2-x1
    dy = y2-y1
    swap_x_y = False
    if x1 == x2:
        m = 0
    else:
        m = dy / dx
    if m > 1:
        swap_x_y = True
        x,y,x1,x2,y1,y2 = y,x,y1,y2,x1,x2
        m = 1 / m
    b = y - m * x1
    if x1 == x2:
        while y <= y2:
            L.append(Cors(x1,y))
            y=y+1
    elif y1 == y2:
        while x <= x2:
            L.append(Cors(x,y1))
            x = x+1
    else:
        while x < x2:
            L.append(Cors(x,y))
            x = x+1
            y = round(m*x +b)
    if (swap_x_y):
        for cors in L:
            cors.x,cors.y = cors.y,cors.x 
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
    x = x1
    y = y1
    dx = x2-x1
    dy = y2-y1
    m = dy / dx
    ne= 2*dy - dx
    L = []
    i = 0
    while i <= dx:
        L.append(Cors(x,y))
        while ne > 0:
            y = y + 1
            ne = ne - 2*dx
        x = x + 1
        ne = ne + 2*dy
        i = i + 1
    return L


def draw_pixels(surface,L,color):
    for cors in L:
        surface.set_at((cors.x, cors.y), color)
    return True

def draw_squares(surface,width,height,cell_size):
    squares = []
    i = 0
    for x in range(0,int(width),cell_size):
        j = 0
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
selectedAlgorithm = SLOPE_INTERCEPT
selectedColor = RED
selectedMode = BOARD
color = RED
# Draw a red rectangle that resizes with the window.
height = surface.get_height()
width = surface.get_width()
Rects = []
ButtonsAlgorithms = [
    Button(surface,Cors(width / 2 + 25,height * 1 / 5),180,30,SLOPE_INTERCEPT),
    Button(surface,Cors(width / 2 + 25,height * 2 / 5),180,30,DIGITAL_ANALYZER),
    Button(surface,Cors(width / 2 + 25,height * 3 / 5),180,30,BRESENHAM)
]

ButtonsColors = [
    Button(surface,Cors(width / 2 + 25,height * 4 / 5),60,30,RED_TEXT),
    Button(surface,Cors(width / 2 + 95,height * 4 / 5),60,30,BLUE_TEXT),
    Button(surface,Cors(width / 2 + 165,height * 4 / 5),80,30,GREEN_TEXT)
]

ButtonMode = [
    Button(surface,Cors(width / 2 + 200,height * 2 / 5),180,30,BOARD),
    Button(surface,Cors(width / 2 + 200,height * 3 / 5),180,30,EMPTY),
]
    
buttonClear = Button(surface,Cors(width / 2 + 300,height * 1 / 5),80,30,CLEAR)
activateButton(ButtonsColors,selectedColor)
activateButton(ButtonsAlgorithms,selectedAlgorithm)
activateButton(ButtonMode,selectedMode)
selectedPoints = []
while True:
    surface.fill((255,255,255))
    color = getColor(selectedColor)
    height = surface.get_height()
    width = surface.get_width()
    
    ButtonsAlgorithms[0].pos = Cors(width / 2 + 25,height * 1 / 5)
    ButtonsAlgorithms[1].pos = Cors(width / 2 + 25,height * 2 / 5)
    ButtonsAlgorithms[2].pos = Cors(width / 2 + 25,height * 3 / 5)

    ButtonsColors[0].pos = Cors(width / 2 + 25,height * 4 / 5)
    ButtonsColors[1].pos = Cors(width / 2 + 95,height * 4 / 5)
    ButtonsColors[2].pos = Cors(width / 2 + 165,height * 4 / 5)

    ButtonMode[0].pos = Cors(width / 2 + 300,height * 2 / 5)
    ButtonMode[1].pos = Cors(width / 2 + 300,height * 3 / 5)

    buttonClear.pos = Cors(width / 2 + 300,height * 1 / 5)
    
    point1 = width/2, height
    point2 = width/2, 0
    lineWidth = surface.get_width()/100

    L = []

    if (selectedMode == BOARD):
        squares = draw_squares(surface,width/2,height,BOARD_CELL_SIZE)

    

    for rect in Rects:
        if selectedMode == BOARD:
            draw_at_positions(surface,squares,rect.L,rect.color)
        elif selectedMode == EMPTY:
            draw_pixels(surface,rect.L,rect.color)

    buttonClear.draw()
   
    for button in ButtonsAlgorithms:
       button.draw()
    
    for button in ButtonsColors:
        button.draw()

    for button in ButtonMode:
        button.draw()

    if (len(selectedPoints) == 2):
        if selectedAlgorithm == SLOPE_INTERCEPT:
            L = slope_intercept(selectedPoints[0].x,selectedPoints[0].y,selectedPoints[1].x,selectedPoints[1].y)
        if selectedAlgorithm == DIGITAL_ANALYZER:
            L = digital_differential_analyzer(selectedPoints[0].x,selectedPoints[0].y,selectedPoints[1].x,selectedPoints[1].y)
        if selectedAlgorithm == BRESENHAM:
            L = bresenham(selectedPoints[0].x,selectedPoints[0].y,selectedPoints[1].x,selectedPoints[1].y)
        Rects.append(Rect(L,selectedColor))
        selectedPoints = []
        L = []

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            cors = Cors(x,y)
            if (cors.x < width / 2):
                selectedPoints.append(cors)
            else:
                if buttonClear.isClicked(cors):
                    Rects = []
                for button in ButtonsAlgorithms:
                    if button.isClicked(cors):
                        selectedAlgorithm = button.text
                        activateButton(ButtonsAlgorithms,selectedAlgorithm)
                for button in ButtonsColors:
                    if button.isClicked(cors):
                        selectedColor = button.text
                        activateButton(ButtonsColors,selectedColor)
                for button in ButtonMode:
                    if button.isClicked(cors):
                        selectedMode = button.text
                        activateButton(ButtonMode,selectedMode)
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



    