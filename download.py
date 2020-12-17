import pygame
from pygame.draw import *
from objects import d, WHITE

back1 = pygame.image.load("back1.png")
back1 = pygame.transform.scale(back1, (d, d))
back2 = pygame.image.load("back2.png")
back2 = pygame.transform.scale(back2, (d, d))
back3 = pygame.image.load("back3.png")
back3 = pygame.transform.scale(back3, (d, d))
dorm = pygame.image.load("dormitory.jpg")

h1 = pygame.image.load("player/1.png")
h1 = pygame.transform.scale(h1, (d, d))
h1.set_colorkey(WHITE)

h2 = pygame.image.load("player/2.png")
h2 = pygame.transform.scale(h2, (d, d))
h2.set_colorkey(WHITE)

h3 = pygame.image.load("player/3.png")
h3 = pygame.transform.scale(h3, (d, d))
h3.set_colorkey(WHITE)

h4 = pygame.image.load("player/4.png")
h4 = pygame.transform.scale(h4, (d, d))
h4.set_colorkey(WHITE)

h5 = pygame.image.load("player/5.png")
h5 = pygame.transform.scale(h5, (d, d))
h5.set_colorkey(WHITE)

h6 = pygame.image.load("player/6.png")
h6 = pygame.transform.scale(h6, (d, d))
h6.set_colorkey(WHITE)

h7 = pygame.image.load("player/7.png")
h7 = pygame.transform.scale(h7, (d, d))
h7.set_colorkey(WHITE)

h8 = pygame.image.load("player/8.png")
h8 = pygame.transform.scale(h8, (d, d))
h8.set_colorkey(WHITE)

h9 = pygame.image.load("player/9.png")
h9 = pygame.transform.scale(h9, (d, d))
h9.set_colorkey(WHITE)

h10 = pygame.image.load("player/10.png")
h10 = pygame.transform.scale(h10, (d, d))
h10.set_colorkey(WHITE)

h11 = pygame.image.load("player/11.png")
h11 = pygame.transform.scale(h11, (d, d))
h11.set_colorkey(WHITE)

h12 = pygame.image.load("player/12.png")
h12 = pygame.transform.scale(h12, (d, d))
h12.set_colorkey(WHITE)

h13 = pygame.image.load("13.png")
h13 = pygame.transform.scale(h13, (d, d))
h13.set_colorkey(WHITE)

h14 = pygame.image.load("14.png")
h14 = pygame.transform.scale(h14, (d, d))
h14.set_colorkey(WHITE)

h15 = pygame.image.load("rat/15.png")
h15 = pygame.transform.scale(h15, (d, d))
h15.set_colorkey(WHITE)

h16 = pygame.image.load("rat/16.png")
h16 = pygame.transform.scale(h16, (d, d))
h16.set_colorkey(WHITE)

h17 = pygame.image.load("rat/17.png")
h17 = pygame.transform.scale(h17, (d, d))
h17.set_colorkey(WHITE)

h18 = pygame.image.load("rat/18.png")
h18 = pygame.transform.scale(h18, (d, d))
h18.set_colorkey(WHITE)

h19 = pygame.image.load("19.png")
h19 = pygame.transform.scale(h19, (d, d))
h19.set_colorkey(WHITE)

h20 = pygame.image.load("20.png")
h20 = pygame.transform.scale(h20, (d, d))
h20.set_colorkey(WHITE)

h21 = pygame.image.load("21.png")
h21 = pygame.transform.scale(h21, (d, int(2*d)))
h21.set_colorkey(WHITE)

h22 = pygame.image.load("22.png")
h22 = pygame.transform.scale(h22, (int(6*d), int(5*d)))
h22.set_colorkey(WHITE)

h23 = pygame.image.load("23.png")
h23 = pygame.transform.scale(h23, (int(6*d), int(5*d)))
h23.set_colorkey(WHITE)

ivanovnik = pygame.image.load('ivanovnik.png')
ivanovnik = pygame.transform.scale(ivanovnik, (d, d))
ivanovnik.set_colorkey(WHITE)

# Endings

ivanov = pygame.image.load("Endings/Ivanov.jpeg")
ivanov = pygame.transform.scale(ivanov, 600, 800)
ivanov.set_colorkey(WHITE)

kiselev = pygame.image.load("Endings/Kiselev.jpg")
kiselev = pygame.transform.scale(kiselev, 600, 800)
kiselev.set_colorkey(WHITE)

karasev = pygame.image.load("Endings/Karasev.jpg")
karasev = pygame.transform.scale(karasev, 600, 800)
karasev.set_colorkey(WHITE)

kojevnikov = pygame.image.load("Endings/Kojevnikov.jpg")
kojevnikov = pygame.transform.scale(kojevnikov, 600, 800)
kojevnikov.set_colorkey(WHITE)

arutunov = pygame.image.load("Endings/Arutunov.jpg")
arutunov = pygame.transform.scale(arutunov, 600, 800)
arutunov.set_colorkey(WHITE)

survive = pygame.image.load("Endings/Survive.jpg")
survive = pygame.transform.scale(survive, 600, 800)
survive.set_colorkey(WHITE)
