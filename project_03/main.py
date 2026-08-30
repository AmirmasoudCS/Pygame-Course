import pygame
import os
import time
import time
pygame.font.init()


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Fonts
MAIN_FONT = pygame.font.SysFont("comicsans", 30)


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


# Abstract Ships Class

class Ship:

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.ship_width = 50
        self.ship_height = 50

    def draw(self, window):
        pygame.draw.rect(window, RED, (self.x, self.y, self.ship_width, self.ship_height))

## Player Ship Class

class Player(Ship):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_BULLET
        self.x_vel = 5

    def move_left(self):
        self.x -= self.x_vel

    def move_right(self):
        self.x += self.x_vel
# Main Loop

def main():

    run = True    
    level = 1
    lives = 5
    clock = pygame.time.Clock()

    ship = Player(WIDTH/2, HEIGHT - 55)

    def redraw_window(*, level, lives):

        # Draw BG
        
        WIN.blit(BACKGROUND, (0, 0))

        # Draw Text
        
        level_labels = MAIN_FONT.render(f"Level: {level}", 1, WHITE)
        lives_label = MAIN_FONT.render(f"Lives: {lives}", 1, WHITE)

        WIN.blit(level_labels, (WIDTH - level_labels.get_width() - 10, 0))
        WIN.blit(lives_label, (10, 0))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window(level=level, lives=lives)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT] and ship.x - ship.x_vel >= 0:     # Left
            ship.move_left()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and ship.x + ship.x_vel <= WIDTH - ship.ship_width:    # Right
            ship.move_right()


# Running the main

if __name__ == "__main__":
    main()
