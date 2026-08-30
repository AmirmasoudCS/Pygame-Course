import pygame
import os
import time
import time

FPS = 60

# Load images

## Enemy Ships

RED_SPACE_SHIP = pygame.image.load("./project_03/assets/pixel_ship_red_small.png")
RED_BULLET = pygame.image.load("./project_03/assets/pixel_laser_red.png")

BLUE_SPACE_SHIP = pygame.image.load("./project_03/assets/pixel_ship_blue_small.png")
BLUE_BULLET = pygame.image.load("./project_03/assets/pixel_laser_blue.png")

GREEN_SPACE_SHIP = pygame.image.load("./project_03/assets/pixel_ship_green_small.png")
GREEN_BULLET = pygame.image.load("./project_03/assets/pixel_laser_green.png")


## Player Ship

YELLOW_SPACE_SHIP = pygame.image.load("./project_03/assets/pixel_ship_yellow.png")
YELLOW_BULLET = pygame.image.load("./project_03/assets/pixel_laser_yellow.png")

## Background

BACKGROUND = pygame.image.load("./project_03/assets/background-black.png")


# Window

WIDTH = 750
HEIGHT = 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Main Loop

def main():

    run = True    
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
