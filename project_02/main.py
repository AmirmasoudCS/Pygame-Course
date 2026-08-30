import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle Ship")

FPS = 60

WHITE = (255, 255, 255)

SHIPS_WIDTH = 55
SHIPS_HEIGT = 40

YELLOW_SPACESHIP = pygame.image.load("./project_02/assets/spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SHIPS_WIDTH, SHIPS_HEIGT))

RED_SPACESHIP = pygame.image.load("./project_02/assets/spaceship_red.png")
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SHIPS_WIDTH, SHIPS_HEIGT))

def draw():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (WIDTH/4, HEIGHT/2))
    WIN.blit(RED_SPACESHIP, (WIDTH-WIDTH/4, HEIGHT/2))
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