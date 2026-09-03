import pygame
import math
from project_04.utils import blit_rotate_center
import pygame
import math
import json
from project_04.utils import blit_rotate_center
pygame.font.init()

PATH_FILE = "./project_04/assets/computer_path.json"

DEV_MODE = False

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
        car_rect.x += 12
        car_rect.y += 21

        offset = (
            car_rect.x - int(x),
            car_rect.y - int(y)
        )

        return mask.overlap(car_mask, offset)

    def bounce(self):
        self.vel = -self.vel

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0

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

class ComputerCar(AbstractCar):
    START_POS = (230, 200)
    IMG = RED_CAR

    def __init__(self, max_vel, rotation_vel, path=None):
        super().__init__(max_vel, rotation_vel)
        self.path = path if path is not None else []
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, window):
        if not self.path:
            return

        if len(self.path) > 1:
            pygame.draw.lines(
                window,
                (255, 100, 100),
                False,
                self.path,
                2
            )

        for i, point in enumerate(self.path):
            pygame.draw.circle(
                window,
                (255, 100, 100),
                point,
                5
            )

            # Highlight current target
            if i == self.current_point:
                pygame.draw.circle(
                    window,
                    (255, 255, 0),
                    point,
                    8,
                    2
                )

    def follow_path(self):
        if len(self.path) < 2:
            return

        nearest_index = min(
            range(len(self.path)),
            key=lambda i: math.hypot(
                self.path[i][0] - self.x,
                self.path[i][1] - self.y
            )
        )

        self.current_point = nearest_index

        look_ahead = 2
        target_index = (nearest_index + look_ahead) % len(self.path)

        target_x, target_y = self.path[target_index]

        dx = target_x - self.x
        dy = target_y - self.y

        target_angle = math.degrees(
            math.atan2(-dx, -dy)
        )

        angle_difference = (
            target_angle - self.angle + 180
        ) % 360 - 180

        if angle_difference > 0:
            self.angle += min(
                self.rotation_vel,
                angle_difference
            )
        elif angle_difference < 0:
            self.angle -= min(
                self.rotation_vel,
                -angle_difference
            )

        self.vel = self.max_vel
        self.move()

    def draw(self, win):
        super().draw(win)

        if DEV_MODE:
            self.draw_points(win)

def draw(window):
    for image, position in IMAGES:
        window.blit(image, position)

    player_car.draw(window)
    computer_car.draw(window)

    if race_finished:
        font = pygame.font.Font(None, 60)
        text = font.render(
            f"{winner} Wins!",
            True,
            (255, 255, 255)
        )
        text_rect = text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )
        window.blit(text, text_rect)

    if DEV_MODE:
        draw_debug(window)


def draw_debug(window):
    # Border mask
    draw_mask_outline(window, BORDER_MASK, BORDER_RECT)

    # Border rectangle
    pygame.draw.rect(window, (255, 0, 0), BORDER_RECT, 2)

    # Finish rectangle
    pygame.draw.rect(window, (0, 255, 0), FINISH_RECT, 2)

    # Actual rotated car rectangle
    rotated_image = pygame.transform.rotate(
        player_car.img,
        player_car.angle
    )

    car_rect = rotated_image.get_rect(
        center=(player_car.x, player_car.y)
    )

    # Manual collision alignment adjustments
    car_rect.x += 12
    car_rect.y += 21

    pygame.draw.rect(window, (0, 0, 255), car_rect, 2)


def draw_mask_outline(window, mask, rect):
    mask_surface = mask.to_surface(
        setcolor=(255, 0, 0, 100),
        unsetcolor=(0, 0, 0, 0)
    )
    window.blit(mask_surface, rect)


def move_player(player_car):
    keys = pygame.key.get_pressed()

    moved = False

    old_x = player_car.x
    old_y = player_car.y

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

    if player_car.collide(
        BORDER_MASK,
        BORDER_RECT.x,
        BORDER_RECT.y
    ):
        player_car.x = old_x
        player_car.y = old_y
        player_car.bounce()

def save_path(path):
    with open(PATH_FILE, "w") as file:
        json.dump(path, file, indent=4)

    print(f"Path saved to: {PATH_FILE}")
    print(f"Saved {len(path)} points")


def load_path():
    try:
        with open(PATH_FILE, "r") as file:
            return [tuple(point) for point in json.load(file)]
    except FileNotFoundError:
        return []


player_car = PlayerCar(3, 3)
computer_car = ComputerCar(2.75, 3, load_path())

race_finished = False
winner = None

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if DEV_MODE and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    computer_car.path.append(pos)

            if event.type == pygame.KEYDOWN:
                if DEV_MODE and event.key == pygame.K_s:
                    save_path(computer_car.path)

                if DEV_MODE and event.key == pygame.K_c:
                    computer_car.path.clear()
                    computer_car.current_point = 0

                if DEV_MODE and event.key == pygame.K_r:
                    computer_car.current_point = 0
                    computer_car.x, computer_car.y = computer_car.START_POS
                    computer_car.angle = 0

        global race_finished
        global winner

        if not race_finished:
            move_player(player_car)
            computer_car.follow_path()

        player_finish = player_car.collide(
            FINISH_MASK,
            *FINISH_POSITION
        )
        computer_finish = computer_car.collide(
            FINISH_MASK,
            *FINISH_POSITION
        )
        if player_finish is not None:
            race_finished = True
            winner = "Player"

        elif computer_finish is not None:
            race_finished = True
            winner = "Computer"

        draw(WIN)
        pygame.display.update()

    if DEV_MODE:
        save_path(computer_car.path)
    pygame.quit()


if __name__ == "__main__":
    main()