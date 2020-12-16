import pygame
from pygame.draw import *
from pygame.locals import *
from PIL import Image
from visual import *

from objects import Hero, Background, d, WHITE, BLACK, GREEN, Moneta, h14, Rat
from download import dorm

pygame.init()
FPS = 30

image = Image.open("karta.png")
height = 15
width = 21
pix = image.load()
l1, l2 = image.size

screen = pygame.display.set_mode((600, 800))
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 72)
hero = Hero(47,42)
background = Background()
monets = []
for i in range(l1):
    for j in range(l2):
        if pix[i,j][:-1] == GREEN:
            monets.append(Moneta(i,j))

f1 = pygame.font.Font(None, 36)
rats = [Rat(0, 0.4, 4 , 4, 52, 60)]

exit_button = Button(0, height*d+10, 'Back to menu')
pause_button = Button(width*d//2, height*d+10, 'Pause')
exit_button.draw()
pause_button.draw()
e1 = exit_button.w
e2 = exit_button.h
exit_button.x += (width * d // 2 - e1) // 2
exit_button.y += (100 - e2) // 2
e1 = pause_button.w
e2 = pause_button.h
pause_button.x += (width * d // 2 - e1) // 2
pause_button.y += (100 - e2) // 2


def game(player):
    sc = 0
    time = 0
    global exit_button, pause_button, monets
    finished = False
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
        screen.fill(WHITE)
        background.draw(screen, pix, hero.x, hero.y, width, height)
        for moneta in monets:
            moneta.draw(screen, hero.x, hero.y, width, height)
        hero.draw(screen, width, height)
        pause_button.draw()
        exit_button.draw()
        x1 = hero.x
        y1 = hero.y
        monets_new = []
        for moneta in monets:
            if moneta.check(hero.x, hero.y):
                sc += 1
            else:
                monets_new += [moneta]
        monets = monets_new
        for i in rats:
            i.calculate()
            if i.drawandcheck(screen, x1, y1):
                finished = True
        screen.blit(f1.render(str(sc) , 1, (0, 0, 0)), (400, 640))
        screen.blit(h14, (340, 630))
        pygame.display.update()
        clock.tick(FPS)
        if not paused:
            keys = pygame.key.get_pressed()
            hero.move(keys, FPS, pix, background)
    inp = open('players.txt', 'a')
    inp.write(player+' '+str(sc)+'\n')
    inp.close
    start_menu()


def start_menu():
    w = 600
    l = 800
    screen = pygame.display.set_mode((w, l))
    global dorm
    dorm = pygame.transform.scale(dorm, (w, l))
    x, y = w, l
    x = x // 5
    y = y // 5
    start_button = Button(x*2, y*2, 'Play')
    end_button = Button(x*2, y*3, 'Exit')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check():
                    name = name_menu()
                    screen = pygame.display.set_mode((width*d, height*d+100))
                    game(name)
                if end_button.check():
                    pygame.quit()
                    raise SystemExit
        dorm_rect = dorm.get_rect(topleft=(0, 0))
        screen.blit(dorm, dorm_rect)
        start_button.draw()
        end_button.draw()
        clock.tick(FPS)
        pygame.display.update()
        screen.fill(WHITE)


def name_menu():
    w = 300
    l = 300
    screen = pygame.display.set_mode((w, l))
    f1 = pygame.font.Font(None, 40)
    text1 = f1.render('What is your name?', True, BLACK)
    name_input = InputBox(75, 140, 150)
    ok_button = Button(0, 200, 'OK')
    ok_button.draw()
    e1 = ok_button.w
    e2 = ok_button.h
    ok_button.x += (w - e1) // 2
    ok_button.y += (100 - e2) // 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.check():
                    return name_input.text
                    start_menu()
            name_input.event_handler(event)
        ok_button.draw()
        name_input.draw()
        screen.blit(text1, (15, 70))
        clock.tick(FPS)
        pygame.display.update()
        screen.fill(WHITE)


start_menu()
