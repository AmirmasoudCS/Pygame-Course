import pygame
import time
from project_05.checkers.constants import (
    WIDTH,
    HEIGHT,
    ROWS,
    COLS,
    WHITE,
    BLACK,
    BLUE,
    RED,
    FPS,
)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def main():

    run = True
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)
        pass
    
