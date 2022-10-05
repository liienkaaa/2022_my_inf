
import pygame
from pygame.draw import *
from house import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))


def draw_sky(screen, color, x,y, width, height): 
    rect(screen, (color),(x,y, width, height))

def draw_grass(screen, color, x,y, width, height): 
    rect(screen, (color), (x,y, width, height))
    
def draw_tree_leaves(screen, color, x,y,radius):
    circle(screen,(color),(x-20,y+20),radius)
    circle(screen,(color),(x+20,y+20),radius)
    circle(screen,(color),(x,y+40),radius)
    circle(screen,(color),(x,y),radius)
    circle(screen,(color),(x-20,y+50),radius)
    circle(screen,(color),(x+17,y+50),radius)

def draw_tree_leaves_border(screen,color,x,y,radius, tolshina):
    circle(screen,(color),(x-20,y+20), radius, tolshina)
    circle(screen,(color),(x+20,y+20),radius, tolshina)
    circle(screen,(color),(x,y+40),radius, tolshina)
    circle(screen,(color),(x,y),radius, tolshina)
    circle(screen,(color),(x-20,y+50),radius, tolshina)
    circle(screen,(color),(x+17,y+50),radius, tolshina)

def draw_tree_basis(screen, color, x,y,width,height):
    rect(screen,(color), (x,y,width,height))
    polygon(screen, (color), [(x,y),(x+7.5 , y),(x+15,y+6),(x,y)])

def draw_cloud(screen,color,x,y,radius):
    circle(screen,(color),(x,y),radius)
    circle(screen,(color),(x+20,y),radius)
    circle(screen,(color),(x+40,y),radius)
    circle(screen,(color),(x+60,y),radius)
    circle(screen,(color),(x+20,y-20),radius)
    circle(screen,(color),(x+40,y-20),radius)

def draw_cloud_border(screen,color,x,y,radius, tolshina):
    circle(screen,(color),(x,y),radius, tolshina)
    circle(screen,(color),(x+20,y),radius, tolshina)
    circle(screen,(color),(x+40,y),radius, tolshina)
    circle(screen,(color),(x+60,y),radius, tolshina)
    circle(screen,(color),(x+20,y-20),radius, tolshina)
    circle(screen,(color),(x+40,y-20),radius, tolshina)
    



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True