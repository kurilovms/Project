import pygame
from pygame.draw import *
from pygame.locals import *
from PIL import Image

from objects import Hero, Background

pygame.init()

FPS = 30
d = 100

image = Image.open("karta.png")
width0, height0 = image.size
height = d * height0
width = d * width0
pix = image.load()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

screen = pygame.display.set_mode((width, height))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
font = pygame.font.Font(None, 72)
hero = Hero(47,42)
background = Background(0, 0, width0, height0)

def game():
    global finished
    while not finished:
        background.draw(screen, pix, hero.x, hero.y)
        hero.draw(screen, background)
        pygame.display.update()
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        keys = pygame.key.get_pressed()
        hero.move(keys, FPS, pix, background)

    pygame.quit()

game()
