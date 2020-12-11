# coding: utf-8
# license: GPLv3
import pygame
from pygame.draw import *

d = 40

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

from download import back1, back2, back3
from download import h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12

back1 = pygame.image.load("back1.png")
back1 = pygame.transform.scale(back1, (d, d))
back2 = pygame.image.load("back2.png")
back2 = pygame.transform.scale(back2, (d, d))
back3 = pygame.image.load("back3.png")
back3 = pygame.transform.scale(back3, (d, d))


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
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and pix[x, y - 1] != (0, 0, 0, 255):
            self.y -= 1
            self.direction = 'backward'
            if self.left_leg:
                self.im = h5
                self.left_leg = False
            else:
                self.im = h6
                self.left_leg = True
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and pix[x, y + 1] != (0, 0, 0, 255):
            self.y += 1
            self.direction = 'forward'
            if self.left_leg:
                self.im = h2
                self.left_leg = False
            else:
                self.im = h3
                self.left_leg = True
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and pix[x - 1, y] != (0, 0, 0, 255):
            self.x -= 1
            self.direction = 'leftward'
            if self.left_leg:
                self.im = h11
                self.left_leg = False
            else:
                self.im = h12
                self.left_leg = True
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and pix[x + 1, y] != (0, 0, 0, 255):
            self.x += 1
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

    def draw(self, sc, width, height):
        dx = (width - 1) / 2
        dy = (height - 1) / 2
        im = self.im
        image_rect = im.get_rect(topleft=(d * dx, d * dy))
        sc.blit(im, image_rect)


class Background():
    def draw(self, sc, pix, x, y, width, height):
        dx = (width - 1) / 2
        dy = (height - 1) / 2
        for i in range(width):
            for j in range(height):
                if pix[x + i - dx, y + j - dy][:-1] == BLACK:
                    image_rect = back1.get_rect(topleft=(d * i, d * j))
                    sc.blit(back1, image_rect)
                elif pix[x + i - dx, y + j - dy][:-1] == RED:
                    image_rect = back2.get_rect(topleft=(d * i, d * j))
                    sc.blit(back2, image_rect)
                elif pix[x + i - dx, y + j - dy][:-1] == WHITE:
                    image_rect = back3.get_rect(topleft=(d * i, d * j))
                    sc.blit(back3, image_rect)
