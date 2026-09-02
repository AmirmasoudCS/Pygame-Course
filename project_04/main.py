import pygame
import time
import math

GRASS = pygame.image.load("assets/imgs/grass.jpg")
TRACK = pygame.image.load("assets/imgs/track.png")
BORDER = pygame.image.load("assets/imgs/track-border.png")
FINISH = pygame.image.load("assets/imgs/finish.png")
RED_CAR = pygame.image.load("assets/imgs/red-car.png")
PURPLE_CAR = pygame.image.load("assets/imgs/purple-car.png")

WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

FPS = 60

def main():

    clock = pygame.time.Clock()

    run = True
    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()