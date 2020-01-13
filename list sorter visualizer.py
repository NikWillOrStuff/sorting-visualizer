import pygame
import math
import pygame.gfxdraw
import time
import sys
import random

# graphics settings
width = 1000
height = 400
size = (width, height)
gap = 1

# sorting settings
listlength = 20
algorithm = 2
sleeptime = .1  # in seconds


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

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sorting visualizer")

mainlist = []
for item in range(listlength):
    mainlist.append(item + 1)
random.shuffle(mainlist)
print_bars(mainlist)

if algorithm == 0:  # bogo sort (scramble until solved)
    count = 0
    while True:
        sorted = True
        for i, bar in enumerate(mainlist):
            if i < 1:
                continue
            if mainlist[i] < mainlist[i - 1]:
                sorted = False
                break
        if sorted:
            print("Iteration count:", count)
            break
        random.shuffle(mainlist)
        print_bars(mainlist)
        update()
        count += 1
        time.sleep(sleeptime)


elif algorithm == 1:
    i = 1
    while i < len(mainlist):
        j = i
        while j > 0 and mainlist[j] < mainlist[j - 1]:
            mainlist[j], mainlist[j - 1] = mainlist[j - 1], mainlist[j]
            print_bars(mainlist)
            update()
            time.sleep(sleeptime)
            j -= 1
        i += 1


elif algorithm == 2:  # selection sort
    i = 0
    while i < len(mainlist):
        j = i + 1
        minimum = i
        while j < len(mainlist):
            if (mainlist[j] < mainlist[minimum]):
                minimum = j
            j += 1
        mainlist[i], mainlist[minimum] = mainlist[minimum], mainlist[i]
        print_bars(mainlist)
        update()
        time.sleep(sleeptime)
        i += 1


print_bars(mainlist)
print("Sorted!")
time.sleep(1)
