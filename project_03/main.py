import pygame
import os
import time
import time
pygame.font.init()


# Fonts
MAIN_FONT = pygame.font.SysFont("comicsans", 50)


# Window

FPS = 60

WIDTH = 750
HEIGHT = 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

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
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))


# Main Loop

def main():

    run = True    
    level = 1
    lives = 5
    clock = pygame.time.Clock()

    def redraw_window(level, lives):

        # Draw BG
        WIN.blit(BACKGROUND, (0, 0))

        # Draw Text
        level_labels = MAIN_FONT.render(f"Level: {level}")
        lives_label = MAIN_FONT.render(f"Lives: {lives}")

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


# Running the main

if __name__ == "__main__":
    main()
