import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle Ship")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

# Background
BG = pygame.image.load("./project_02/assets/space.png")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

BULLET_VEL = 7
MAX_BULLETS = 3

SHIPS_WIDTH = 55
SHIPS_HEIGHT = 40

SHIPS_X_VEL = 5
SHIPS_Y_VEL = 3

# Yellow spaceship
YELLOW_SPACESHIP = pygame.image.load(
    "./project_02/assets/spaceship_yellow.png"
)
YELLOW_SPACESHIP = pygame.transform.scale(
    YELLOW_SPACESHIP,
    (SHIPS_WIDTH, SHIPS_HEIGHT)
)
YELLOW_SPACESHIP = pygame.transform.rotate(
    YELLOW_SPACESHIP,
    90
)

YELLOW_SPACESHIP_X = WIDTH // 4
YELLOW_SPACESHIP_Y = HEIGHT // 2

YELLOW_HIT = pygame.USEREVENT + 1

# Red spaceship
RED_SPACESHIP = pygame.image.load(
    "./project_02/assets/spaceship_red.png"
)
RED_SPACESHIP = pygame.transform.scale(
    RED_SPACESHIP,
    (SHIPS_WIDTH, SHIPS_HEIGHT)
)
RED_SPACESHIP = pygame.transform.rotate(
    RED_SPACESHIP,
    270
)

RED_SPACESHIP_X = WIDTH - WIDTH // 4
RED_SPACESHIP_Y = HEIGHT // 2

RED_HIT = pygame.USEREVENT + 2


def handle_bullets(yellow_bullets, red_bullets, yellow, red):

    # Yellow bullets
    for bullet in yellow_bullets[:]:
        bullet.x += BULLET_VEL

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    # Red bullets
    for bullet in red_bullets[:]:
        bullet.x -= BULLET_VEL

        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw(yellow, red, yellow_bullets, red_bullets):

    # Draw background
    WIN.blit(BG, (0, 0))

    # Draw border
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Draw spaceships
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    # Draw yellow bullets
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    # Draw red bullets
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()


def main():

    yellow_bullets = []
    red_bullets = []

    yellow = pygame.Rect(
        YELLOW_SPACESHIP_X,
        YELLOW_SPACESHIP_Y,
        SHIPS_WIDTH,
        SHIPS_HEIGHT
    )

    red = pygame.Rect(
        RED_SPACESHIP_X,
        RED_SPACESHIP_Y,
        SHIPS_WIDTH,
        SHIPS_HEIGHT
    )

    clock = pygame.time.Clock()

    run = True

    while run:

        clock.tick(FPS)

        # -------------------------
        # Events
        # -------------------------

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                # Yellow shoots with Left Alt
                if (
                    event.key == pygame.K_LALT
                    and len(yellow_bullets) < MAX_BULLETS
                ):
                    bullet = pygame.Rect(
                        yellow.x + SHIPS_WIDTH,
                        yellow.y + SHIPS_HEIGHT // 2,
                        10,
                        5
                    )

                    yellow_bullets.append(bullet)

                # Red shoots with Right Alt
                if (
                    event.key == pygame.K_RALT
                    and len(red_bullets) < MAX_BULLETS
                ):
                    bullet = pygame.Rect(
                        red.x,
                        red.y + SHIPS_HEIGHT // 2,
                        10,
                        5
                    )

                    red_bullets.append(bullet)

        # -------------------------
        # Movement
        # -------------------------

        keys_pressed = pygame.key.get_pressed()

        # Yellow spaceship - WASD

        if keys_pressed[pygame.K_a] and yellow.x - SHIPS_X_VEL >= 0:
            yellow.x -= SHIPS_X_VEL

        if (
            keys_pressed[pygame.K_d]
            and yellow.x + SHIPS_X_VEL
            <= BORDER.left - SHIPS_WIDTH
        ):
            yellow.x += SHIPS_X_VEL

        if keys_pressed[pygame.K_w] and yellow.y - SHIPS_Y_VEL >= 0:
            yellow.y -= SHIPS_Y_VEL

        if (
            keys_pressed[pygame.K_s]
            and yellow.y + SHIPS_Y_VEL
            <= HEIGHT - SHIPS_HEIGHT
        ):
            yellow.y += SHIPS_Y_VEL

        # Red spaceship - Arrow keys

        if (
            keys_pressed[pygame.K_LEFT]
            and red.x - SHIPS_X_VEL >= BORDER.right
        ):
            red.x -= SHIPS_X_VEL

        if (
            keys_pressed[pygame.K_RIGHT]
            and red.x + SHIPS_X_VEL
            <= WIDTH - SHIPS_WIDTH
        ):
            red.x += SHIPS_X_VEL

        if keys_pressed[pygame.K_UP] and red.y - SHIPS_Y_VEL >= 0:
            red.y -= SHIPS_Y_VEL

        if (
            keys_pressed[pygame.K_DOWN]
            and red.y + SHIPS_Y_VEL
            <= HEIGHT - SHIPS_HEIGHT
        ):
            red.y += SHIPS_Y_VEL

        # -------------------------
        # Bullets
        # -------------------------

        handle_bullets(
            yellow_bullets,
            red_bullets,
            yellow,
            red
        )

        # -------------------------
        # Draw
        # -------------------------

        draw(
            yellow,
            red,
            yellow_bullets,
            red_bullets
        )

    pygame.quit()


if __name__ == "__main__":
    main()