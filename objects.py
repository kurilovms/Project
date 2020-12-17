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
GRAY = (195, 195, 195)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE, GRAY]

from download import back1, back2, back3
from download import h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12,\
    h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, ivanovnik


class Hero():
    """Тип данных, описывающий главного героя"""
    def __init__(self, x=0, y=0):
        """
        Args: x, y - координаты главного героя

        """
        self.x = x
        self.y = y
        self.im = h1
        self.left_leg = True
        self.direction = 'forward'

    def move(self, keys, FPS, pix, background):
        """
        Описывает движение главного героя
        Он упирается в стены и шагает, останавливается при ненажатых клавишах
        Управление стрелочками или кнопками W, A, S, D

        Agrs:   keys - данные, позволяющие зажимать клавиши, а не нажимать их каждый раз
                pix - массив, соответствующий карте

        """
        x = self.x
        y = self.y
        if (keys[pygame.K_w] or keys[pygame.K_UP])\
                and pix[x, y - 1] != (0, 0, 0, 255):
            self.y -= 1
            self.direction = 'backward'
            if self.left_leg:
                self.im = h5
                self.left_leg = False
            else:
                self.im = h6
                self.left_leg = True
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN])\
                and pix[x, y + 1] != (0, 0, 0, 255):
            self.y += 1
            self.direction = 'forward'
            if self.left_leg:
                self.im = h2
                self.left_leg = False
            else:
                self.im = h3
                self.left_leg = True
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT])\
                and pix[x - 1, y] != (0, 0, 0, 255):
            self.x -= 1
            self.direction = 'leftward'
            if self.left_leg:
                self.im = h11
                self.left_leg = False
            else:
                self.im = h12
                self.left_leg = True
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT])\
                and pix[x + 1, y] != (0, 0, 0, 255):
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
        """
        Выводит изображение главного героя на экран

        Agrs:   sc - объект pygame.Surface
                width - ширина экрана в d
                height - высота экрана в d

        """
        dx = (width - 1) / 2
        dy = (height - 1) / 2
        im = self.im
        image_rect = im.get_rect(topleft=(d * dx, d * dy))
        sc.blit(im, image_rect)


class Moneta():
    """Тип данных, описывающий монету"""
    def __init__(self, x=0, y=0):
        """
        Args:   x, y - координаты монеты

        """
        self.x = x
        self.y = y
        self.x0 = x
        self.y0 = y
        self.im = h13

    def draw(self, sc, x1, y1, width, height):
        """
        Выводит изображение монеты на экран

        Agrs:   sc - объект pygame.Surface
                x1, y1 - координаты главного героя
                width - ширина экрана в d
                height - высота экрана в d

        """
        dx = self.x - x1 + (width-1)/2
        dy = self.y - y1 + (height-1)/2
        if 0 <= dx <= width and 0 <= dy < height:
            im = self.im
            image_rect = im.get_rect(topleft=(d*dx, d*dy))
            sc.blit(im, image_rect)

    def check(self, x1, y1):
        """
        Проверяется, взял ли главный герой эту монету
        Если взял, то монета помещается за экран, функция возвращает True

        Agrs:   x1, y1 - координаты главного героя

        """
        if self.x == x1:
            if self.y == y1:
                self.x = -1
                self.y = -1
                return True

    def recovery(self):
        """Восстанавливает изначальное положение монет"""
        self.x = self.x0
        self.y = self.y0


class Rat():
    """Тип данных, описывающий крысу"""
    def __init__(self, spdx=0, spdy=0, dx=0, dy=0, x0=0, y0=0):
        """
        Args:   x0, y0 - начальные координаты крысы
                spdx - начальная скорость крысы вдоль оси x
                spdy - начальная скорость крысы вдоль оси y
                dx - максимальное отклонение от начального положения вдоль оси x
                dy - максимальное отклонение от начального положения вдоль оси y

                """
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
        """
        Реализуется движение крысы
        Крыса двигатся только вдоль ox или oy
        Разворачивает крысу, если она отошла от начального положения на амплитудное значение

        """
        self.x += self.spdx
        self.y += self.spdy
        if abs(self.x - self.x0) > self.dx:
            self.spdx = -self.spdx
        if abs(self.y - self.y0) > self.dy:
            self.spdy = -self.spdy

    def draw(self, sc, x1, y1, width, height):
        """
        Выводит изображение крысы на экран

        Agrs:   sc - объект pygame.Surface
                x1, y1 - координаты главного героя
                width - ширина экрана в d
                height - высота экрана в d

        """
        dx = self.x - x1 + (width - 1) / 2
        dy = self.y - y1 + (height - 1) / 2
        if 0 <= dx <= width and 0 <= dy < height:
            if self.spdy == 0:
                if self.spdx > 0:
                    im = self.im2
                else:
                    im = self.im1
            if self.spdx == 0:
                if self.spdy > 0:
                    im = self.im4
                else:
                    im = self.im3
            image_rect = im.get_rect(topleft=(d * dx, d * dy))
            sc.blit(im, image_rect)

    def check(self, x1, y1):
        """
        Проверяется, столкнулся ли главный герой с крысой
        Если столкнулся, то функция возвращает True

        Agrs:   x1, y1 - координаты главного героя

        """
        if abs(self.x - x1) < 1 and abs(self.y - y1) < 1:
            return True


class Matan():
    """Тип данных, описывающий задание по матану"""
    def __init__(self, x=0, y=0):
        """
        Args:   x, y - координаты задания

        """
        self.x = x
        self.y = y
        self.im = h19

    def draw(self, sc, x1, y1, width, height):
        """
        Выводит изображение задания

        Agrs:   sc - объект pygame.Surface
                x1, y1 - координаты главного героя
                width - ширина экрана в d
                height - высота экрана в d

        """
        dx = self.x - x1 + (width - 1) / 2
        dy = self.y - y1 + (height - 1) / 2
        if 0 <= dx <= width and 0 <= dy < height:
            im = self.im
            image_rect = im.get_rect(topleft=(d * dx, d * dy))
            sc.blit(im, image_rect)

    def check(self, x1, y1):
        """
        Проверяется, взял ли главный герой это задание
        Если взял, то задание помещается за экран, функция возвращает True

        Agrs:   x1, y1 - координаты главного героя

        """
        if self.x == x1 and self.y == y1:
            self.x = -1
            self.y = -1
            return True


class Ivanovnik(Matan):
    """Тип данных, описывающий учебник Г. Е. Иванова"""
    def __init__(self, x=0, y=0):
        """
        Args:   x, y - координаты учебника

        """
        self.x = x
        self.y = y
        self.im = ivanovnik


class Npc():
    """Тип данных, описывающий преподавателя"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.im = h21
        self.im1 = h22
        self.im2 = h23

    def draw(self, sc, x1, y1, width, height, matan, ivanovnik):
        """
        Выводит изображение преподавателя на экран

        Agrs:   sc - объект pygame.Surface
                x1, y1 - координаты главного героя
                width - ширина экрана в d
                height - высота экрана в d

        """
        dx = self.x - x1 + (width - 1) / 2
        dy = self.y - y1 + (height - 1) / 2
        if 0 <= dx <= width and 0 <= dy < height:
            im = self.im
            image_rect = im.get_rect(topleft=(d * dx, d * dy))
            sc.blit(im, image_rect)
        if abs(self.x - x1) <= 1 and abs(self.y - y1) <= 1:
            if matan < 3:
                im = self.im1
            else:
                im = self.im2
            image_rect = im.get_rect(topleft=(d * (dx + 0.4), d * (dy - 5)))
            sc.blit(im, image_rect)

    def check(self, x1, y1, matan):
        """
        Если герой подходит к преподавателю, проверяется, есть ли у героя все 3 задания
        Если да, функция возвращает True

        Agrs:   x1, y1 - координаты главного героя
                matan - количество заданий у героя

        """
        if abs(self.x - x1) <= 1 and abs(self.y - y1) <= 1 and matan == 3:
            return True


class Background():
    """Тип данных, описывающий фон"""
    def draw(self, sc, pix, x, y, width, height):
        """
        Рисует фон вокруг игрока

        Agrs:
            pix - массив, соответствующий карте
            x, y - координаты главного героя
            width - ширина экрана в d
            height - высота экрана в d

        """
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
                elif (pix[x + i - dx, y + j - dy][:-1] == BLUE)\
                        or (pix[x + i - dx, y + j - dy][:-1] == GREEN):
                    image_rect = back3.get_rect(topleft=(d * i, d * j))
                    sc.blit(back3, image_rect)
