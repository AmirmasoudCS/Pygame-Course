import pygame
import random
import math
import time

pygame.init()
pygame.font.init()

FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4

RECT_HEIGHT, RECT_WIDTH = HEIGHT // ROWS, WIDTH // 2

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BG_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

FONT = pygame.font.SysFont("comicsans", 60, bold=True)

MOVE_VEL = 20 

def draw(window):

    window.fill(BG_COLOR)

    pygame.display.update()

def main(window):

    run = True
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)

        draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()

if __name__ == "__main__":
    main(WIN)