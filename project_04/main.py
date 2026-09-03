import pygame
import time
import math
from project_04.utils import blit_rotate_center

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
BORDER_MASK = pygame.mask.from_surface(BORDER)
BORDER_MASK_RECT = BORDER_MASK.get_rect(center=WIN.get_rect().center)

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
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def move_forward(self):
        self.vel = min(self.vel+self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        rotated_image = pygame.transform.rotate(self.img, self.angle)
        car_mask = pygame.mask.from_surface(rotated_image)

        car_rect = rotated_image.get_rect(center=(self.x, self.y))

        offset = (
            car_rect.x - int(x),
            car_rect.y - int(y)
        )

        return mask.overlap(car_mask, offset)

    def bounce(self):
        self.vel = -self.vel
        self.move()

    def draw(self, window):
        blit_rotate_center(window, self.img, (self.x, self.y), self.angle)

class PlayerCar(AbstractCar):

    START_POS = (190, 200)
    IMG = PURPLE_CAR

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2, 0)
        self.move()

def draw(window, images, player_car):

    for image, pos in images:
        window.blit(image, pos)

    player_car.draw(window)
    pygame.display.update()

def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()

player_car = PlayerCar(3, 3)

def main():

    clock = pygame.time.Clock()

    draw(WIN, images, player_car)

    pygame.display.update()

    run = True
    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        move_player(player_car)

        if player_car.collide(BORDER_MASK, BORDER_RECT.x, BORDER_RECT.y) != None:
            player_car.bounce()
        
        draw(WIN, images, player_car)

    pygame.quit()


if __name__ == "__main__":
    main()