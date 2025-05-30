import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Guess the symbol")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



Symbols = ["+", "-", "*", "/"]

rows = 3
columns = 3

for i in range(rows):
    for j in range(columns):
        print(random.choice(Symbols), end=" ")
    print()

