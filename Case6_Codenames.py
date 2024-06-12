#PythonGeeks - Import Modules
import random
import pygame
import sys
from pygame.locals import *


Frame_Speed = 30 
Window_Width = 640 
Window_Height = 480 
Speed_Reveal = 8 
Box_Size = 40 
Gap_Size = 10
Border_Width = 10 
Border_Height = 7 

assert (Border_Width * Border_Height) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
X_margin = int((Window_Width - (Border_Width * (Box_Size + Gap_Size))) / 2)
Y_margin = int((Window_Height - (Border_Height * (Box_Size + Gap_Size))) / 2)

#            R    G    B
Gray     = (100, 100, 100)
Navyblue = ( 60,  60, 100)
White    = (255, 255, 255)
Red      = (255,   0,   0)
Green    = (  0, 255,   0)
Blue     = (  0,   0, 255)
Yellow   = (255, 255,   0)
Orange   = (255, 128,   0)
Purple   = (255,   0, 255)
Cyan     = (  0, 255, 255)

BackGround_color = Gray
Light_BackGround_color = Navyblue
Box_Color = Cyan
HighLight_Color = Yellow

CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'


All_Colors = (Red, Green, Blue, Yellow, Orange, Purple, Cyan)
All_Shapes = (CIRCLE, SQUARE, DIAMOND, LINES, OVAL)
assert len(All_Colors)* len(All_Shapes) * 2 >= Border_Width * Border_Height, "Board is too big for the number of shapes/colors defined."

def main():
    global Frame_Speed_Clock, DIS_PlaySurf
    pygame.init()
    Frame_Speed_Clock = pygame.time.Clock()
    DIS_PlaySurf = pygame.display.set_mode((Window_Width, Window_Height))
 
    X_mouse  = 0 
    Y_mouse = 0 
    pygame.display.set_caption('Memory Game by PythonGeeks')
 
    #@Board = Randomized_Board()
    #Boxes_revealed = GenerateData_RevealedBoxes(False)
 
    first_Selection = None  
    DIS_PlaySurf.fill(BackGround_color)
    #Start_Game(Board)
 
if __name__ == '__main__':
    main()