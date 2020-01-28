'''
Qazi Umer Jamil
317920
NUST RIME SMME
'''

import pygame #for GUI framework
import copy

#Initialize PyGame Environment
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
done = False #for quiting pygame window

#Fonts for dislaying various texts
font = pygame.font.SysFont("comicsansms", 60)
fontState = pygame.font.SysFont("comicsansms", 30)
fontTitle = pygame.font.SysFont("comicsansms", 45)


def convertArray(arr):
    rslt = arr
    for i in range(0,3):
        for j in range(0,3):
            if arr[i][j] == 0:
                rslt[i][j] = "_"
    return rslt 

#Func to display puzzle state on the PyGame window
def displayPuzzzle(STATE):
    STATE = convertArray(copy.deepcopy(STATE))
    pos00 = font.render(str(STATE[0][0]), True, (255, 255, 255))
    pos01 = font.render(str(STATE[0][1]), True, (255, 255, 255))
    pos02 = font.render(str(STATE[0][2]), True, (255, 255, 255))
    pos10 = font.render(str(STATE[1][0]), True, (255, 255, 255))
    pos11 = font.render(str(STATE[1][1]), True, (255, 255, 255))
    pos12 = font.render(str(STATE[1][2]), True, (255, 255, 255))

    pos20 = font.render(str(STATE[2][0]), True, (255, 255, 255))
    pos21 = font.render(str(STATE[2][1]), True, (255, 255, 255))
    pos22 = font.render(str(STATE[2][2]), True, (255, 255, 255))

    screen.blit(pos00,
        (280 - pos00.get_width() // 2, 160 - pos00.get_height() // 2))
    screen.blit(pos01,
        (350 - pos01.get_width() // 2, 160 - pos01.get_height() // 2))
    screen.blit(pos02,
        (420 - pos02.get_width() // 2, 160 - pos02.get_height() // 2))

    screen.blit(pos10,
        (280 - pos10.get_width() // 2, 220 - pos10.get_height() // 2))
    screen.blit(pos11,
        (350 - pos11.get_width() // 2, 220 - pos11.get_height() // 2))
    screen.blit(pos12,
        (420 - pos12.get_width() // 2, 220 - pos12.get_height() // 2))

    screen.blit(pos20,
        (280 - pos20.get_width() // 2, 280 - pos20.get_height() // 2))
    screen.blit(pos21,
        (350 - pos21.get_width() // 2, 280 - pos21.get_height() // 2))
    screen.blit(pos22,
        (420 - pos22.get_width() // 2, 280 - pos22.get_height() // 2))

#Func to display Start state on the PyGame window
def displayStartState(STATE):
    STATE = convertArray(copy.deepcopy(STATE))
    pos00 = font.render(str(STATE[0][0]), True, (255, 255, 255))
    pos01 = font.render(str(STATE[0][1]), True, (255, 255, 255))
    pos02 = font.render(str(STATE[0][2]), True, (255, 255, 255))
    pos10 = font.render(str(STATE[1][0]), True, (255, 255, 255))
    pos11 = font.render(str(STATE[1][1]), True, (255, 255, 255))
    pos12 = font.render(str(STATE[1][2]), True, (255, 255, 255))

    pos20 = font.render(str(STATE[2][0]), True, (255, 255, 255))
    pos21 = font.render(str(STATE[2][1]), True, (255, 255, 255))
    pos22 = font.render(str(STATE[2][2]), True, (255, 255, 255))

    screen.blit(pos00,
        (50 - pos00.get_width() // 2, 160 - pos00.get_height() // 2))
    screen.blit(pos01,
        (120 - pos01.get_width() // 2, 160 - pos01.get_height() // 2))
    screen.blit(pos02,
        (190 - pos02.get_width() // 2, 160 - pos02.get_height() // 2))

    screen.blit(pos10,
        (50 - pos10.get_width() // 2, 220 - pos10.get_height() // 2))
    screen.blit(pos11,
        (120 - pos11.get_width() // 2, 220 - pos11.get_height() // 2))
    screen.blit(pos12,
        (190 - pos12.get_width() // 2, 220 - pos12.get_height() // 2))

    screen.blit(pos20,
        (50 - pos20.get_width() // 2, 280 - pos20.get_height() // 2))
    screen.blit(pos21,
        (120 - pos21.get_width() // 2, 280 - pos21.get_height() // 2))
    screen.blit(pos22,
        (190 - pos22.get_width() // 2, 280 - pos22.get_height() // 2))

#Func to display Goal State on the PyGame window
def displayGoalState(STATE):
    STATE = convertArray(copy.deepcopy(STATE))
    pos00 = font.render(str(STATE[0][0]), True, (255, 255, 255))
    pos01 = font.render(str(STATE[0][1]), True, (255, 255, 255))
    pos02 = font.render(str(STATE[0][2]), True, (255, 255, 255))
    pos10 = font.render(str(STATE[1][0]), True, (255, 255, 255))
    pos11 = font.render(str(STATE[1][1]), True, (255, 255, 255))
    pos12 = font.render(str(STATE[1][2]), True, (255, 255, 255))

    pos20 = font.render(str(STATE[2][0]), True, (255, 255, 255))
    pos21 = font.render(str(STATE[2][1]), True, (255, 255, 255))
    pos22 = font.render(str(STATE[2][2]), True, (255, 255, 255))

    screen.blit(pos00,
        (520 - pos00.get_width() // 2, 160 - pos00.get_height() // 2))
    screen.blit(pos01,
        (590 - pos01.get_width() // 2, 160 - pos01.get_height() // 2))
    screen.blit(pos02,
        (660 - pos02.get_width() // 2, 160 - pos02.get_height() // 2))

    screen.blit(pos10,
        (520 - pos10.get_width() // 2, 220 - pos10.get_height() // 2))
    screen.blit(pos11,
        (590 - pos11.get_width() // 2, 220 - pos11.get_height() // 2))
    screen.blit(pos12,
        (660 - pos12.get_width() // 2, 220 - pos12.get_height() // 2))

    screen.blit(pos20,
        (520 - pos20.get_width() // 2, 280 - pos20.get_height() // 2))
    screen.blit(pos21,
        (590 - pos21.get_width() // 2, 280 - pos21.get_height() // 2))
    screen.blit(pos22,
        (660 - pos22.get_width() // 2, 280 - pos22.get_height() // 2))

#Func to display Text/Titles on the PyGame window
def displayTitles():
    pygame.draw.rect(screen, (255,0,0), (30,130,190,175))
    pygame.draw.rect(screen, (0,255,0), (260,130,190,175))
    pygame.draw.rect(screen, (0,0,255), (490,130,190,175))

    start = fontState.render("INITAL STATE", True, (0, 0, 0))
    screen.blit(start,
    (120 - start.get_width() // 2, 320 - start.get_height() // 2))

    current = fontState.render("CURRENT STATE", True, (0, 0, 0))
    screen.blit(current,
    (350 - current.get_width() // 2, 320 - current.get_height() // 2))

    end = fontState.render("GOAL STATE", True, (0, 0, 0))
    screen.blit(end,
    (580 - end.get_width() // 2, 320 - end.get_height() // 2))

    start = fontTitle.render("8 Puzzle Problem using A*- Search", True, (0, 0, 0))
    screen.blit(start,
    (360 - start.get_width() // 2, 50 - start.get_height() // 2))

def diplayResult(str):
    start = fontTitle.render(str, True, (0, 0, 0))
    screen.blit(start,
    (360 - start.get_width() // 2, 420 - start.get_height() // 2))
