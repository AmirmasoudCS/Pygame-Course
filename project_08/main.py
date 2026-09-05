import os
import random
import pygame
import math
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

WHITE = (255, 255, 255)
BG_COLOR = WHITE

WIDTH, HEIGHT = 1000, 800

FPS = 60

PLAYER_VEL = 5

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    pygame.quit()


if __name__ == "__main__":
    main()
