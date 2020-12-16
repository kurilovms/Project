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
from download import h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18


class Hero():
    """Тип данных, описывающий главного героя."""
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

class Moneta():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.im = h13

    def draw(self, sc, x1, y1, width, height):
        dx = self.x - x1 + (width-1)/2
        dy = self.y - y1 + (height-1)/2
        if 0 <= dx <= width and 0 <= dy < height:
            im = self.im
            image_rect = im.get_rect(topleft=(d*dx, d*dy))
            sc.blit(im, image_rect)

    def check(self, x1, y1):
        if self.x == x1:
            if self.y == y1:
                self.x = -1
                self.y = -1
                return True

class Rat():
    def __init__(self, spdx=0, spdy=0, dx=0, dy=0, x0=0, y0=0):
        self.x = x0
        self.y = y0
        self.spdx = spdx
        self.spdy = spdy
        self.im1 = h15
        self.im2 = h16
        self.im3 = h17
        self.im4 = h18
        self.dx = dx
        self.dy = dy
        self.x0 = x0
        self.y0 = y0

    def calculate(self):
        self.x+= self.spdx
        self.y+= self.spdy
        if self.x > self.x0 + self.dx or self.x < self.x0 - self.dx:
           self.spdx = -self.spdx
        if self.y > self.y0 + self.dy or self.y < self.y0 -self.dy:
            self.spdy = -self.spdy

    def drawandcheck(self, sc, x1, y1):
        dx = self.x - x1
        dy = self.y - y1
        if self.spdy == 0:
            if self.spdx > 0:
                im = self.im2
            else:
                im= self.im1
        if self.spdx == 0:
            if self.spdy > 0:
                im = self.im4
            else:
                im = self.im3
        image_rect = im.get_rect(topleft=(d * dx, d * dy))
        sc.blit(im, image_rect)
        if self.x - x1 < 11 and self.x - x1  > 9:
            if self.y - y1 < 8 and self.y - y1 > 6:
                return True

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
                elif pix[x + i - dx, y + j - dy][:-1] == GREEN:
                    image_rect = back3.get_rect(topleft=(d * i, d * j))
                    sc.blit(back3, image_rect)
