import pygame
import time
import math

TRACK = pygame.image.load("./project_04/assets/imgs/track.png")
BORDER = pygame.image.load("./project_04/assets/imgs/track-border.png")
FINISH = pygame.image.load("./project_04/assets/imgs/finish.png")
RED_CAR = pygame.image.load("./project_04/assets/imgs/red-car.png")
PURPLE_CAR = pygame.image.load("./project_04/assets/imgs/purple-car.png")

CAR_WIDTH = RED_CAR.get_width()
CAR_HEIGHT = RED_CAR.get_height()

SCALE_FACTOR = 0.6

RED_CAR = pygame.transform.scale(RED_CAR, (SCALE_FACTOR*CAR_WIDTH, SCALE_FACTOR*CAR_HEIGHT))
PURPLE_CAR = pygame.transform.scale(PURPLE_CAR, (SCALE_FACTOR*CAR_WIDTH, SCALE_FACTOR*CAR_HEIGHT))


MARGIN = 50

WIDTH = TRACK.get_width() + MARGIN  
HEIGHT = TRACK.get_height() + MARGIN

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

GRASS = pygame.transform.scale(pygame.image.load("./project_04/assets/imgs/grass.jpg"), (WIDTH, HEIGHT))

GRASS_RECT = GRASS.get_rect(center=WIN.get_rect().center)
TRACK_RECT = TRACK.get_rect(center=WIN.get_rect().center)
BORDER_RECT = BORDER.get_rect(center=WIN.get_rect().center)

FPS = 60

def main():

    clock = pygame.time.Clock()

    WIN.blit(GRASS, GRASS_RECT)
    WIN.blit(TRACK, TRACK_RECT)
    WIN.blit(BORDER, BORDER_RECT)
    WIN.blit(PURPLE_CAR, (0, 0))

    pygame.display.update()

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