from pygame.draw import *

def draw_house_wall(screen, color, x, y, width, height):   
    rect(screen, color, (x, y, width, height))

def draw_house_wall_border(screen, color, x, y, width, height, tolshina): 
    rect(screen, color, (x, y, width, height), tolshina)

def draw_house_window(screen, color, x, y, width, height): 
    rect(screen, color, (x, y, width, height))

def draw_house_window_border(screen, color, x, y, width, height, tolshina): 
    rect(screen, color, (x, y, width, height), tolshina)

def draw_house_roof(screen, color, x1,y1, x2,y2, x3,y3, x4,y4): 
    polygon(screen, color, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)])

def draw_house_roof_border(screen, color, x1,y1, x2,y2, x3,y3, x4,y4, tolshina): 
    polygon(screen, color, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], tolshina)
