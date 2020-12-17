import pygame
import sys
import tkinter as tk
from pygame.draw import *
from pygame.locals import *
from PIL import Image
from visual import *

from objects import Hero, Background, d, WHITE, BLACK, GREEN, BLUE, Moneta,\
    Rat, Matan, Npc, Ivanovnik
from download import dorm, ratat, ded, h14, h20, ivanovnik

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
f1 = pygame.font.Font(None, 36)
background = Background()
monets = []
ivanovnics = []
for i in range(l1):
    for j in range(l2):
        if pix[i, j][:-1] == GREEN:
            monets.append(Moneta(i, j))
        if pix[i, j][:-1] == BLUE:
            ivanovnics.append(Ivanovnik(i, j))

exit_button = Button(0, height*d+10, 'Back to menu')
pause_button = Button(width*d//2, height*d+10, 'Pause')
exit_button.draw()
pause_button.draw()
e1 = exit_button.w
e2 = exit_button.h
exit_button.x += -50 + (width * d // 2 - e1) // 2
exit_button.y += (100 - e2) // 2
e1 = pause_button.w
e2 = pause_button.h
pause_button.x += 50 + (width * d // 2 - e1) // 2
pause_button.y += (100 - e2) // 2

matans = [Matan(79, 33), Matan(131, 37), Matan(115, 114)]
npc = Npc(66, 70)


def game(player):
    if player == '':
        player = 'nan'
    hero = Hero(71, 70)
    rats = [Rat(0.05, 0, 1, 0, 49, 65),
            Rat(0.1, 0, 1, 0, 51, 61),
            Rat(0.2, 0, 1, 0, 49, 57),
            Rat(0, 0.2, 0, 3, 20, 49),
            Rat(0, -0.2, 0, 3, 18, 49),
            Rat(0, 0.2, 0, 4, 72, 33),
            Rat(0, 0.1, 0, 4, 139, 35),
            Rat(0, 0.05, 0, 2, 144, 34),
            Rat(0, 0.1, 0, 3, 150, 36),
            Rat(0, 0.1, 0, 3, 155, 36),
            Rat(0, 0.05, 0, 2, 168, 46),
            Rat(0, 0.1, 0, 2, 156, 99),
            Rat(0, -0.1, 0, 2, 152, 97),
            Rat(0, 0.1, 0, 2, 148, 99),
            Rat(0, -0.1, 0, 2, 144, 97),
            Rat(0, 0.2, 0, 3, 110, 101),
            Rat(0, 0.1, 0, 2, 193, 127),
            Rat(0, 0.2, 0, 2, 114, 79)]
    sc = 0
    sc1 = 0
    sc2 = 0
    trigger = False
    global exit_button, pause_button, monets, ivanovnics, matans
    finished = False
    paused = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise sys.exit()
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
        for moneta in monets:
            if moneta.check(hero.x, hero.y):
                sc += 1
        for rat in rats:
            if rat.check(hero.x, hero.y):
                finished = True
                die_menu(sc, sc1, sc2)
        for matan in matans:
            if matan.check(hero.x, hero.y) is True:
                sc1 += 1
        for book in ivanovnics:
            if book.check(hero.x, hero.y):
                sc2 += 1
        if npc.check(hero.x, hero.y, sc1):
            trigger = True

        screen.fill(WHITE)
        background.draw(screen, pix, hero.x, hero.y, width, height)
        for rat in rats:
            rat.draw(screen, hero.x, hero.y, width, height)
        for moneta in monets:
            moneta.draw(screen, hero.x, hero.y, width, height)
        for matan in matans:
            matan.draw(screen, hero.x, hero.y, width, height)
        for book in ivanovnics:
            book.draw(screen, hero.x, hero.y, width, height)
        pause_button.draw()
        exit_button.draw()
        screen.blit(f1.render(str(sc), 1, BLACK), (350, 640))
        screen.blit(h14, (290, 630))
        screen.blit(f1.render(str(sc1) + '/3', 1, BLACK), (450, 640))
        screen.blit(h20, (395, 630))
        screen.blit(f1.render(str(sc2) + '/11', 1, BLACK), (550, 640))
        screen.blit(ivanovnik, (495, 630))
        hero.draw(screen, width, height)
        npc.draw(screen, hero.x, hero.y, width, height, sc1, sc2)
        pygame.display.update()
        clock.tick(FPS)
        for rat in rats:
            rat.calculate()
        if not paused:
            keys = pygame.key.get_pressed()
            hero.move(keys, FPS, pix, background)
        if trigger:
            finished = True
            pygame.time.wait(1000)
            win_menu(sc, sc1, sc2)
    inp = open('players.txt', 'a')
    inp.write(player + ' ' + str(sc) + ' ' + str(sc1) + ' ' + str(sc2) + '\n')
    inp.close


def start_menu():
    w = 600
    l = 600
    screen = pygame.display.set_mode((w, l))
    global dorm
    dorm = pygame.transform.scale(dorm, (w, l))
    x, y = w, l
    x = x // 5
    y = y // 5
    start_button = Button(x*2, y*2, 'Play')
    end_button = Button(x*2, y*4, 'Exit')
    results_button = Button(x*1.5, y*3, 'Best scores')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check():
                    name = name_menu()
                    screen = pygame.display.set_mode((width*d, height*d+100))
                    game(name)
                    screen = pygame.display.set_mode((w, l))
                if results_button.check():
                    best_scores()
                if end_button.check():
                    pygame.quit()
                    raise sys.exit()
        dorm_rect = dorm.get_rect(topleft=(0, 0))
        screen.blit(dorm, dorm_rect)
        start_button.draw()
        results_button.draw()
        end_button.draw()
        clock.tick(FPS)
        pygame.display.update()
        screen.fill(WHITE)


def die_menu(s, s1, s2):
    w = 300
    l = 400
    global ratat
    ratat = pygame.transform.scale(ratat, (w, l))
    screen = pygame.display.set_mode((w, l))
    f1 = pygame.font.Font(None, 40)
    text1 = f1.render('ВЫ УМЕРЛИ!', True, BLACK)
    text2 = f1.render('Ваш счет:', True, BLACK)
    ok_button = Button(50, 320, 'OK')
    back = False
    while not back:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.check():
                    back = True
        clock.tick(FPS)
        ratat_rect = ratat.get_rect(topleft=(0, 0))
        screen.blit(ratat, ratat_rect)
        screen.blit(text1, (50, 50))
        screen.blit(text2, (50, 100))
        screen.blit(f1.render(str(s), 1, BLACK), (100, 150))
        screen.blit(h14, (50, 150))
        screen.blit(f1.render(str(s1) + '/3', 1, BLACK), (100, 200))
        screen.blit(h20, (50, 200))
        screen.blit(f1.render(str(s2) + '/11', 1, BLACK), (100, 250))
        screen.blit(ivanovnik, (50, 250))
        ok_button.draw()
        pygame.display.update()
        screen.fill(WHITE)


def win_menu(s, s1, s2):
    w = 300
    l = 400
    global ded
    ded = pygame.transform.scale(ded, (w, l))
    screen = pygame.display.set_mode((w, l))
    f1 = pygame.font.Font(None, 40)
    text1 = f1.render('ВЫ ВЫЖИЛИ!', True, BLACK)
    text2 = f1.render('Ваш счет:', True, BLACK)
    ok_button = Button(50, 320, 'OK')
    back = False
    while not back:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.check():
                    back = True
        clock.tick(FPS)
        ded_rect = ded.get_rect(topleft=(0, 0))
        screen.blit(ded, ded_rect)
        screen.blit(text1, (50, 50))
        screen.blit(text2, (50, 100))
        screen.blit(f1.render(str(s), 1, BLACK), (100, 150))
        screen.blit(h14, (50, 150))
        screen.blit(f1.render(str(s1) + '/3', 1, BLACK), (100, 200))
        screen.blit(h20, (50, 200))
        screen.blit(f1.render(str(s2) + '/3', 1, BLACK), (100, 250))
        screen.blit(ivanovnik, (50, 250))
        ok_button.draw()
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
                raise sys.exit()
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


def best_scores():
    inp = open('players.txt', 'r')
    if inp.read() != '':
        with open('players.txt') as file:
            res = []
            for j, line in enumerate(file):
                B = line.split()
                name = B[0]
                coins = int(B[1])
                tasks = int(B[2])
                ivs = int(B[3])
                res.append([name, coins, tasks, ivs])
        res = sorted(res, key=lambda i: -i[1])
        with open("players.txt", "w") as file:
            for i in res:
                file.write(i[0]+' '+str(i[1])+' '+str(i[2])+' '+str(i[3])+'\n')
    else:
        res = []
    inp.close()
    res = res[:10]
    root_scores = tk.Tk()
    root_scores.title("Лучшие результаты")
    root_scores.geometry('350x350')
    back = tk.Button(text='Back to menu',
                     command=lambda: root_scores.destroy(),
                     width=10, font='28')
    back.grid(row=0, column=0, columnspan=4, pady=5)
    head_name = tk.Label(root_scores, text=' name ', font='28')
    head_name.grid(row=1, column=0)
    head_score = tk.Label(root_scores, text=' coins ', font='28')
    head_score.grid(row=1, column=1)
    head_shots = tk.Label(root_scores, text=' tasks ', font='28')
    head_shots.grid(row=1, column=2)
    head_shots = tk.Label(root_scores, text=' books ', font='28')
    head_shots.grid(row=1, column=3)
    for i, s in enumerate(res):
        bar_0 = tk.Label(root_scores, text=s[0], font='28')
        bar_0.grid(row=2+i, column=0)
        bar_1 = tk.Label(root_scores, text=s[1], font='28')
        bar_1.grid(row=2+i, column=1)
        bar_2 = tk.Label(root_scores, text=s[2], font='28')
        bar_2.grid(row=2+i, column=2)
        bar_3 = tk.Label(root_scores, text=s[3], font='28')
        bar_3.grid(row=2+i, column=3)
    root_scores.mainloop()


start_menu()
