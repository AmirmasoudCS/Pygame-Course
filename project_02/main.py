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
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP, (SHIPS_WIDTH, SHIPS_HEIGT)), 90)
YELLOW_SPACESHIP_X = WIDTH/4
YELLOW_SPACESHIP_Y = HEIGHT/2


RED_SPACESHIP = pygame.image.load("./project_02/assets/spaceship_red.png")
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP, (SHIPS_WIDTH, SHIPS_HEIGT)), 270)
RED_SPACESHIP_X = WIDTH-WIDTH/4
RED_SPACESHIP_Y = HEIGHT/2

def draw(yellow, red):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def main():

    yellow = pygame.Rect(YELLOW_SPACESHIP_X, YELLOW_SPACESHIP_Y, SHIPS_WIDTH, SHIPS_HEIGT)
    red = pygame.Rect(RED_SPACESHIP_X, RED_SPACESHIP_Y, SHIPS_WIDTH, SHIPS_HEIGT)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        draw(yellow, red)

    pygame.quit()

if __name__ == "__main__":
    main()