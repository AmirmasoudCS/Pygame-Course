import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle Ship")

FPS = 60

WHITE = (255, 255, 255)

YELLOW_SPACESHIP = pygame.image.load("./assets/spaceship_yellow.png")
RED_SPACESHIP = pygame.image.load("./assets/spaceship_red.png")

def draw():
    WIN.fill(WHITE)
    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()