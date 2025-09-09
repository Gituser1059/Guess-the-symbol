import random
import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 815

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill("white")

pygame.display.set_caption("Guess the symbol")
clock = pygame.time.Clock()

# linjer
line_vertical = pygame.Surface((5, SCREEN_HEIGHT))
line_vertical.fill("black")

line_horizontal = pygame.Surface((SCREEN_WIDTH, 5))
line_horizontal.fill("black")

line_seperator = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
line_seperator.fill("purple")

# cirklar
red_circle = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(red_circle, (255, 0, 0), (100, 100), 100)

green_circle = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(green_circle, (0, 255, 0), (100, 100), 100)

blue_circle = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(blue_circle, (0, 0, 255), (100, 100), 100)

circle_list = [red_circle, green_circle, blue_circle]

# rutornas positioner (vänster överhörn för varje ruta)
positions = [
    (0, 0), (250, 0), (525, 0),
    (0, 205), (250, 205), (525, 205),
    (0, 410), (250, 410), (525, 410),
]

# välj slumpad cirkel för varje position
current_circles = [random.choice(circle_list) for _ in positions]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # rita bakgrund + linjer
    screen.fill("white")
    screen.blit(line_seperator, (0, 610))
    screen.blit(line_vertical, (237.5, 0))
    screen.blit(line_vertical, (512.5, 0))
    screen.blit(line_horizontal, (0, 200))
    screen.blit(line_horizontal, (0, 405))

    # rita alla cirklar på sina platser
    for pos, circle in zip(positions, current_circles):
        screen.blit(circle, pos)

    pygame.display.update()
    clock.tick(60)
