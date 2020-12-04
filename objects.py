# coding: utf-8
# license: GPLv3
import pygame
from pygame.draw import *

d = 100

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

back1 = pygame.image.load("back1.png")
back1 = pygame.transform.scale(back1, (d, d))
back2 = pygame.image.load("back2.png")
back2 = pygame.transform.scale(back2, (d, d))
back3 = pygame.image.load("back3.png")
back3 = pygame.transform.scale(back3, (d, d))

h1 = pygame.image.load("1.png")
h1 = pygame.transform.scale(h1, (d, d))
h1.set_colorkey(WHITE)

h2 = pygame.image.load("2.png")
h2 = pygame.transform.scale(h2, (d, d))
h2.set_colorkey(WHITE)

h3 = pygame.image.load("3.png")
h3 = pygame.transform.scale(h3, (d, d))
h3.set_colorkey(WHITE)

h4 = pygame.image.load("4.png")
h4 = pygame.transform.scale(h4, (d, d))
h4.set_colorkey(WHITE)

h5 = pygame.image.load("5.png")
h5 = pygame.transform.scale(h5, (d, d))
h5.set_colorkey(WHITE)

h6 = pygame.image.load("6.png")
h6 = pygame.transform.scale(h6, (d, d))
h6.set_colorkey(WHITE)

h7 = pygame.image.load("7.png")
h7 = pygame.transform.scale(h7, (d, d))
h7.set_colorkey(WHITE)

h8 = pygame.image.load("8.png")
h8 = pygame.transform.scale(h8, (d, d))
h8.set_colorkey(WHITE)

h9 = pygame.image.load("9.png")
h9 = pygame.transform.scale(h9, (d, d))
h9.set_colorkey(WHITE)

h10 = pygame.image.load("10.png")
h10 = pygame.transform.scale(h10, (d, d))
h10.set_colorkey(WHITE)

h11 = pygame.image.load("11.png")
h11 = pygame.transform.scale(h11, (d, d))
h11.set_colorkey(WHITE)

h12 = pygame.image.load("12.png")
h12 = pygame.transform.scale(h12, (d, d))
h12.set_colorkey(WHITE)

class Hero():
    """Тип данных, описывающий главного героя.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.im = h1
        self.left_leg = True
        self.direction = 'forward'

    def move(self, keys, FPS, pix, background):
        x = self.x
        y = self.y
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and pix[x,y-1] != (0,0,0, 255):
            self.y -= 1
            background.y1 += 1
            self.direction = 'backward'
            if self.left_leg:
                self.im = h5
                self.left_leg = False
            else:
                self.im = h6
                self.left_leg = True
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and pix[x,y+1] != (0,0,0, 255):
            self.y += 1
            background.y1 -= 1
            self.direction = 'forward'
            if self.left_leg:
                self.im = h2
                self.left_leg = False
            else:
                self.im = h3
                self.left_leg = True
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and pix[x-1,y] != (0,0,0, 255):
            self.x -= 1
            background.x1 += 1
            self.direction = 'leftward'
            if self.left_leg:
                self.im = h11
                self.left_leg = False
            else:
                self.im = h12
                self.left_leg = True
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and pix[x+1,y] != (0,0,0, 255):
            self.x += 1
            background.x1 -= 1
            self.direction = 'rightward'
            if self.left_leg:
                self.im = h8
                self.left_leg = False
            else:
                self.im = h9
                self.left_leg = True
        else:
            if self.direction == 'forward':
                self.im = h1
            if self.direction == 'backward':
                self.im = h4
            if self.direction == 'leftward':
                self.im = h10
            if self.direction == 'rightward':
                self.im = h7
            
    def draw(self, sc, background):
        x1 = background.x1
        y1 = background.y1
        im = self.im
        image_rect = im.get_rect(topleft=(d*(x1+self.x), d*(y1+self.y)))
        sc.blit(im, image_rect)

class Background():
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height

    def draw(self, sc, pix, x, y, dx=10, dy=10):
        for i in range(max(x-dx, 0), min(x+dx, self.width)):
            for j in range(max(y-dy, 0), min(y+dy, self.height)):
                if pix[i,j][:-1] == BLACK:
                    image_rect = back1.get_rect(topleft=(d*(i+self.x1), d*(j+self.y1)))
                    sc.blit(back1, image_rect)
                elif pix[i,j][:-1] == RED:
                    image_rect = back2.get_rect(topleft=(d*(i+self.x1), d*(j+self.y1)))
                    sc.blit(back2, image_rect)
                elif pix[i,j][:-1] == WHITE:
                    image_rect = back3.get_rect(topleft=(d*(i+self.x1), d*(j+self.y1)))
                    sc.blit(back3, image_rect)
        
        
