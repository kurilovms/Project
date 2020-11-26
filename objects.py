# coding: utf-8
# license: GPLv3
import pygame
from pygame.draw import *

class Hero():
    """Тип данных, описывающий главного героя.
    """
    def __init__(self, a=1, b=1, x=2, y=2):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def move(self, keys, FPS, pix):
        x = self.x
        y = self.y
        a = self.a
        b = self.b
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and pix[x,y-1] != (0,0,0, 255):
            self.y -= 1
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and pix[x,y+1] != (0,0,0, 255):
            self.y += 1
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and pix[x-1,y] != (0,0,0, 255):
            self.x -= 1
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and pix[x+1,y] != (0,0,0, 255):
            self.x += 1
            

    def draw(self, sc, d):
        rect(sc, (0,0,255), (d*self.x, d*self.y, d*self.a, d*self.b))




        
        
