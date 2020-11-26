import pygame
from pygame.draw import *
from pygame.locals import *
from PIL import Image

from objects import Hero

pygame.init()

FPS = 30
d = 10

image = Image.open("karta.png")
width, height = image.size
height = d * height
width = d * width
pix = image.load()

back1 = pygame.image.load("back1.png")
back1 = pygame.transform.scale(back1, (d, d))
back2 = pygame.image.load("back2.png")
back2 = pygame.transform.scale(back2, (d, d))
back3 = pygame.image.load("back3.png")
back3 = pygame.transform.scale(back3, (d, d))

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
hero = Hero()

def draw_background(sc, p):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if pix[i,j][:-1] == BLACK:
                image_rect = back1.get_rect(topleft=(i*p, j*p))
                sc.blit(back1, image_rect)
            elif pix[i,j][:-1] == RED:
                image_rect = back2.get_rect(topleft=(i*p, j*p))
                sc.blit(back2, image_rect)
            elif pix[i,j][:-1] == WHITE:
                image_rect = back3.get_rect(topleft=(i*p, j*p))
                sc.blit(back3, image_rect)

def game():
    global finished
    while not finished:
        hero.draw(screen, d)
        pygame.display.update()
        draw_background(screen, d)
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        keys = pygame.key.get_pressed()
        hero.move(keys, FPS, pix)

    pygame.quit()

game()
