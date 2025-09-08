import random
import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH =  700
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill("red")

pygame.display.set_caption("Guess the symbol")

clock = pygame.time.Clock()

line_vertical = pygame.Surface((5, SCREEN_HEIGHT))
line_vertical.fill("black")

line_vertical2 = pygame.Surface((5, SCREEN_HEIGHT))
line_vertical2.fill("black")

line_horizontal = pygame.Surface((SCREEN_WIDTH, 5))
line_horizontal.fill("black")

line_horizontal2 = pygame.Surface((SCREEN_WIDTH, 5))
line_horizontal2.fill("black")

#line_seperator3 = pygame.Surface((5, SCREEN_HEIGHT))
#line_seperator3.fill("black")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(line_vertical, (225, 0))
    screen.blit(line_vertical2, (475, 0))
    screen.blit(line_horizontal, (0, 266))
    screen.blit(line_horizontal2,(0, 534))

    pygame.display.update()
    clock.tick(60)
