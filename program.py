import pygame
from pygame.draw import *
from pygame.locals import *
from PIL import Image
from visual import *

from objects import Hero, Background, d

pygame.init()

FPS = 30

image = Image.open("karta.png")
width0, height0 = image.size
# следующие 2 параметра обязательно нечетные
height = 15
width = 15
pix = image.load()

screen = pygame.display.set_mode((width*d, height*d))
pygame.display.update()
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 72)
hero = Hero(47,42)
background = Background()

def game(player):
    finished = False
    exit_button = Button(50, 50, 'Back to menu')
    pause_button = Button(50, 200, 'Pause')
    paused = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.check():
                    finished = True
                if pause_button.check():
                    if paused:
                        paused = False
                        pause_button.text = 'Pause'
                    else:
                        paused = True
                        pause_button.text = 'Unpause'
        screen.fill((255, 255, 255))
        pause_button.draw()
        exit_button.draw()
        background.draw(screen, pix, hero.x, hero.y, width, height)
        hero.draw(screen, width, height)
        pygame.display.update()
        clock.tick(FPS)
        if not paused:
            keys = pygame.key.get_pressed()
            hero.move(keys, FPS, pix, background)


def start_menu():
    x, y = pygame.display.get_surface().get_size()
    x = x // 5
    y = y // 5
    Start_button = Button(x * 2, y * 2, 'Play')
    Exit_button = Button(x *2, y * 3, 'Exit')
    Name_input = InputBox(x * 2, y * 4, 150)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Start_button.check():
                    game(Name_input.text)
                    Name_input.text = ''
                if Exit_button.check():
                    pygame.quit()
                    raise SystemExit
            Name_input.event_handler(event)
        Start_button.draw()
        Exit_button.draw()
        Name_input.draw()
        clock.tick(FPS)
        pygame.display.update()
        screen.fill((255, 255, 255))

start_menu()
