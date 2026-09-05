import pygame
import random
import math

pygame.init()

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