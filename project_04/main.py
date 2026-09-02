import pygame
import time
import math
from utils import blit_rotate_center

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

images = [(GRASS,GRASS_RECT), (TRACK, TRACK_RECT), (BORDER, BORDER_RECT)]

class AbstractCar:

    IMG = RED_CAR

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0

    def rotate(self, left=False, right=False):
        
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, window):
        blit_rotate_center(window, self.img)

def draw(window, images):

    for image, pos in images:
        window.blit(image, pos)

def main():

    clock = pygame.time.Clock()

    draw(WIN, images)    

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