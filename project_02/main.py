import pygame

pygame.init()
pygame.mixer.init()
DESTROY_SOUND = pygame.mixer.Sound("./project_02/assets/Grenade+1.mp3")
BULLET_SOUND = pygame.mixer.Sound("./project_02/assets/Gun+Silencer.mp3")


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

MAX_HEALTH = 3

# Font
HEALTH_FONT = pygame.font.SysFont("arial", 30)
WINNER_FONT = pygame.font.SysFont("arial", 60)

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
            DESTROY_SOUND.play()
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    # Red bullets
    for bullet in red_bullets[:]:

        bullet.x -= BULLET_VEL

        if yellow.colliderect(bullet):
            DESTROY_SOUND.play()
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw(
    yellow,
    red,
    yellow_bullets,
    red_bullets,
    yellow_health,
    red_health
):

    # Background
    WIN.blit(BG, (0, 0))

    # Border
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Spaceships
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    # Bullets
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    # Health
    yellow_health_text = HEALTH_FONT.render(
        f"Health: {yellow_health}",
        True,
        YELLOW
    )

    red_health_text = HEALTH_FONT.render(
        f"Health: {red_health}",
        True,
        RED
    )

    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(
        red_health_text,
        (
            WIDTH - red_health_text.get_width() - 10,
            10
        )
    )

    pygame.display.update()


def draw_winner(text):

    winner_text = WINNER_FONT.render(
        text,
        True,
        WHITE
    )

    WIN.blit(
        winner_text,
        (
            WIDTH // 2 - winner_text.get_width() // 2,
            HEIGHT // 2 - winner_text.get_height() // 2
        )
    )

    pygame.display.update()

    pygame.time.delay(3000)


def main():

    yellow_bullets = []
    red_bullets = []

    yellow_health = MAX_HEALTH
    red_health = MAX_HEALTH

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

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            # Yellow shoots
            if event.type == pygame.KEYDOWN:

                if (
                    event.key == pygame.K_LALT
                    and len(yellow_bullets) < MAX_BULLETS
                ):
                    
                    BULLET_SOUND.play()
                    
                    bullet = pygame.Rect(
                        yellow.x + SHIPS_WIDTH,
                        yellow.y + SHIPS_HEIGHT // 2,
                        10,
                        5
                    )

                    yellow_bullets.append(bullet)

                # Red shoots
                if (
                    event.key == pygame.K_RALT
                    and len(red_bullets) < MAX_BULLETS
                ):

                    BULLET_SOUND.play()
                    
                    bullet = pygame.Rect(
                        red.x,
                        red.y + SHIPS_HEIGHT // 2,
                        10,
                        5
                    )

                    red_bullets.append(bullet)

            # Red got hit
            if event.type == RED_HIT:

                red_health -= 1

                if red_health <= 0:

                    winner_text = "YELLOW WINS! RED LOSES!"

                    WIN.fill(BLACK)
                    draw_winner(winner_text)

                    run = False

            # Yellow got hit
            if event.type == YELLOW_HIT:

                yellow_health -= 1

                if yellow_health <= 0:

                    winner_text = "RED WINS! YELLOW LOSES!"

                    WIN.fill(BLACK)
                    draw_winner(winner_text)

                    run = False

        # --------------------------------
        # Movement
        # --------------------------------

        keys_pressed = pygame.key.get_pressed()

        # Yellow - WASD

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

        # Red - Arrow keys

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

        # --------------------------------
        # Bullets
        # --------------------------------

        handle_bullets(
            yellow_bullets,
            red_bullets,
            yellow,
            red
        )

        # --------------------------------
        # Draw
        # --------------------------------

        draw(
            yellow,
            red,
            yellow_bullets,
            red_bullets,
            yellow_health,
            red_health
        )

    pygame.quit()


if __name__ == "__main__":
    main()