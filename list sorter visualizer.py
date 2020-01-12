import pygame
import math
import pygame.gfxdraw
import time
import sys
import random

width = 1000
height = 400
size = (width, height)
gap = 1

listlength = 8
algorithm = 0
sleeptime = 0  # in seconds


pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")


def print_bars(bars):
    screen.fill((0, 0, 0))
    current_X = 0
    next_X = 0
    for i, bar in enumerate(bars):
        current_X = next_X
        next_X = math.ceil((width / listlength) * (i + 1))
        pygame.draw.rect(screen, (100, 100, 100), (
            current_X,                                              # X
            math.ceil((height / listlength) * (listlength - bar)),  # Y
            next_X - current_X - gap,                               # width
            math.floor((height / listlength) * bar)                 # height
            ))
    pygame.display.update()
    # print(bars)


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


mainlist = []
for item in range(listlength):
    mainlist.append(item + 1)

count = 0

if algorithm == 0:  # bogo sort (scramble until solved)
    while True:
        print_bars(mainlist)
        update()
        random.shuffle(mainlist)
        count += 1
        sorted = True
        for i, bar in enumerate(mainlist):
            if i < 1:
                continue
            if mainlist[i] < mainlist[i - 1]:
                sorted = False
                break
        if sorted:
            break
        time.sleep(sleeptime)

elif algorithm == 1:
    pass
print_bars(mainlist)
print("Iteration count:", count)
time.sleep(2)
