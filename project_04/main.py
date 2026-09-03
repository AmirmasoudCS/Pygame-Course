import pygame
import math
from project_04.utils import blit_rotate_center

TRACK = pygame.image.load("./project_04/assets/imgs/track.png")
BORDER = pygame.image.load("./project_04/assets/imgs/track-border.png")
FINISH = pygame.image.load("./project_04/assets/imgs/finish.png")
RED_CAR = pygame.image.load("./project_04/assets/imgs/red-car.png")
PURPLE_CAR = pygame.image.load("./project_04/assets/imgs/purple-car.png")

FINISH_POSITION = (170, 250)
SCALE_FACTOR = 0.6
MARGIN = 50
FPS = 60

CAR_WIDTH = RED_CAR.get_width()
CAR_HEIGHT = RED_CAR.get_height()

RED_CAR = pygame.transform.scale(
    RED_CAR,
    (int(SCALE_FACTOR * CAR_WIDTH), int(SCALE_FACTOR * CAR_HEIGHT))
)
PURPLE_CAR = pygame.transform.scale(
    PURPLE_CAR,
    (int(SCALE_FACTOR * CAR_WIDTH), int(SCALE_FACTOR * CAR_HEIGHT))
)

WIDTH = TRACK.get_width() + MARGIN
HEIGHT = TRACK.get_height() + MARGIN

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

GRASS = pygame.transform.scale(
    pygame.image.load("./project_04/assets/imgs/grass.jpg"),
    (WIDTH, HEIGHT)
)

GRASS_RECT = GRASS.get_rect(center=WIN.get_rect().center)
TRACK_RECT = TRACK.get_rect(center=WIN.get_rect().center)
BORDER_RECT = BORDER.get_rect(center=WIN.get_rect().center)
FINISH_RECT = FINISH.get_rect(topleft=FINISH_POSITION)

BORDER_MASK = pygame.mask.from_surface(BORDER)
FINISH_MASK = pygame.mask.from_surface(FINISH)

IMAGES = [
    (GRASS, GRASS_RECT),
    (TRACK, TRACK_RECT),
    (FINISH, FINISH_POSITION),
    (BORDER, BORDER_RECT)
]


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
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
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

    def draw(self, window):
        blit_rotate_center(
            window,
            self.img,
            (self.x, self.y),
            self.angle
        )


class PlayerCar(AbstractCar):
    START_POS = (190, 200)
    IMG = PURPLE_CAR

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


def draw(window):
    for image, position in IMAGES:
        window.blit(image, position)

    player_car.draw(window)

    # Show border rectangle
    pygame.draw.rect(window, (255, 0, 0), BORDER_RECT, 2)

    # Show finish rectangle
    pygame.draw.rect(window, (0, 255, 0), FINISH_RECT, 2)

    # Show car rectangle
    car_rect = player_car.img.get_rect(center=(player_car.x, player_car.y))
    pygame.draw.rect(window, (0, 0, 255), car_rect, 2)

    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_car.rotate(left=True)

    if keys[pygame.K_d]:
        player_car.rotate(right=True)

    if keys[pygame.K_w]:
        player_car.move_forward()
    elif keys[pygame.K_s]:
        player_car.move_backward()
    else:
        player_car.reduce_speed()


player_car = PlayerCar(3, 3)


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        move_player(player_car)

        if player_car.collide(
            FINISH_MASK,
            FINISH_RECT.x,
            FINISH_RECT.y
        ):
            print("FINISH!")

        draw(WIN)

    pygame.quit()


if __name__ == "__main__":
    main()