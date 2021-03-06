import pygame
from pygame.draw import *
from objects import d, WHITE, GRAY

back1 = pygame.image.load("back1.png")
back1 = pygame.transform.scale(back1, (d, d))
back2 = pygame.image.load("back2.png")
back2 = pygame.transform.scale(back2, (d, d))
back3 = pygame.image.load("back3.png")
back3 = pygame.transform.scale(back3, (d, d))
dorm = pygame.image.load("dormitory.jpg")
ratat = pygame.image.load("ratat.jpg")
ded = pygame.image.load("ded.jpg")

h1 = pygame.image.load("player/1.png")
h1 = pygame.transform.scale(h1, (d, d))
h1.set_colorkey(GRAY)

h2 = pygame.image.load("player/2.png")
h2 = pygame.transform.scale(h2, (d, d))
h2.set_colorkey(GRAY)

h3 = pygame.image.load("player/3.png")
h3 = pygame.transform.scale(h3, (d, d))
h3.set_colorkey(GRAY)

h4 = pygame.image.load("player/4.png")
h4 = pygame.transform.scale(h4, (d, d))
h4.set_colorkey(GRAY)

h5 = pygame.image.load("player/5.png")
h5 = pygame.transform.scale(h5, (d, d))
h5.set_colorkey(GRAY)

h6 = pygame.image.load("player/6.png")
h6 = pygame.transform.scale(h6, (d, d))
h6.set_colorkey(GRAY)

h7 = pygame.image.load("player/7.png")
h7 = pygame.transform.scale(h7, (d, d))
h7.set_colorkey(GRAY)

h8 = pygame.image.load("player/8.png")
h8 = pygame.transform.scale(h8, (d, d))
h8.set_colorkey(GRAY)

h9 = pygame.image.load("player/9.png")
h9 = pygame.transform.scale(h9, (d, d))
h9.set_colorkey(GRAY)

h10 = pygame.image.load("player/10.png")
h10 = pygame.transform.scale(h10, (d, d))
h10.set_colorkey(GRAY)

h11 = pygame.image.load("player/11.png")
h11 = pygame.transform.scale(h11, (d, d))
h11.set_colorkey(GRAY)

h12 = pygame.image.load("player/12.png")
h12 = pygame.transform.scale(h12, (d, d))
h12.set_colorkey(GRAY)

h13 = pygame.image.load("13.png")
h13 = pygame.transform.scale(h13, (d, d))
h13.set_colorkey(GRAY)

h14 = pygame.image.load("14.png")
h14 = pygame.transform.scale(h14, (d, d))
h14.set_colorkey(WHITE)

h15 = pygame.image.load("rat/15.png")
h15 = pygame.transform.scale(h15, (d, d))
h15.set_colorkey(GRAY)

h16 = pygame.image.load("rat/16.png")
h16 = pygame.transform.scale(h16, (d, d))
h16.set_colorkey(GRAY)

h17 = pygame.image.load("rat/17.png")
h17 = pygame.transform.scale(h17, (d, d))
h17.set_colorkey(GRAY)

h18 = pygame.image.load("rat/18.png")
h18 = pygame.transform.scale(h18, (d, d))
h18.set_colorkey(GRAY)

h19 = pygame.image.load("19.png")
h19 = pygame.transform.scale(h19, (d, d))
h19.set_colorkey(GRAY)

h20 = pygame.image.load("20.png")
h20 = pygame.transform.scale(h20, (d, d))
h20.set_colorkey(WHITE)

h21 = pygame.image.load("21.png")
h21 = pygame.transform.scale(h21, (d, int(2*d)))
h21.set_colorkey(GRAY)

h22 = pygame.image.load("22.png")
h22 = pygame.transform.scale(h22, (int(6*d), int(5*d)))
h22.set_colorkey(GRAY)

h23 = pygame.image.load("23.png")
h23 = pygame.transform.scale(h23, (int(6*d), int(5*d)))
h23.set_colorkey(GRAY)

ivanovnik = pygame.image.load('ivanovnik.png')
ivanovnik = pygame.transform.scale(ivanovnik, (d, d))
ivanovnik.set_colorkey(WHITE)
