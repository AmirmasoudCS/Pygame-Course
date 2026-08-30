import pygame
import random

pygame.font.init()


# =========================
# Colors
# =========================

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# =========================
# Fonts
# =========================

MAIN_FONT = pygame.font.SysFont("comicsans", 30)


# =========================
# Window
# =========================

FPS = 60

WIDTH = 750
HEIGHT = 1000

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")


# =========================
# Load Images
# =========================

# Enemy Ships

RED_SPACE_SHIP = pygame.image.load(
    "./project_03/assets/pixel_ship_red_small.png"
)
RED_BULLET = pygame.image.load(
    "./project_03/assets/pixel_laser_red.png"
)

BLUE_SPACE_SHIP = pygame.image.load(
    "./project_03/assets/pixel_ship_blue_small.png"
)
BLUE_BULLET = pygame.image.load(
    "./project_03/assets/pixel_laser_blue.png"
)

GREEN_SPACE_SHIP = pygame.image.load(
    "./project_03/assets/pixel_ship_green_small.png"
)
GREEN_BULLET = pygame.image.load(
    "./project_03/assets/pixel_laser_green.png"
)


# Player Ship

YELLOW_SPACE_SHIP = pygame.image.load(
    "./project_03/assets/pixel_ship_yellow.png"
)
YELLOW_BULLET = pygame.image.load(
    "./project_03/assets/pixel_laser_yellow.png"
)


# Background

BACKGROUND = pygame.image.load(
    "./project_03/assets/background-black.png"
)
BACKGROUND = pygame.transform.scale(
    BACKGROUND,
    (WIDTH, HEIGHT)
)


# =========================
# Laser Base Class
# =========================

def lose():

    run = True

    while run:

        WIN.fill(BLACK)

        lose_label = MAIN_FONT.render(
            "LOST!",
            1,
            RED
        )

        WIN.blit(
            lose_label,
            (
                WIDTH / 2 - lose_label.get_width() / 2,
                HEIGHT / 2 - lose_label.get_height() / 2
            )
        )

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                run = False
class Laser:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.y_vel = 0
        self.damage = 1

    def move(self):
        self.y += self.y_vel

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def off_screen(self):
        return self.y < 0 or self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.image.get_width(),
            self.image.get_height()
        )


# =========================
# Player Laser Class
# =========================

class PlayerLaser(Laser):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.image = YELLOW_BULLET
        self.y_vel = -5
        self.damage = 10


# =========================
# Enemy Laser Class
# =========================

class EnemyLaser(Laser):

    def __init__(self, x, y, image):
        super().__init__(x, y)

        self.image = image
        self.y_vel = 5
        self.damage = 10


# =========================
# Ship Base Class
# =========================

class Ship:

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health

        self.ship_img = None

        # This will be set by the child class
        self.laser_type = None

        # Contains actual Laser objects
        self.lasers = []

        self.cool_down_counter = 0

        self.ship_width = 50
        self.ship_height = 50

    def draw(self, window):

        # Draw the ship
        window.blit(
            self.ship_img,
            (self.x, self.y)
        )

        # Draw all lasers belonging to the ship
        for laser in self.lasers:
            laser.draw(window)

    def shoot(self):

        if self.cool_down_counter == 0:

            laser = self.laser_type(
                self.x + self.ship_width / 2,
                self.y
            )

            self.lasers.append(laser)

            self.cool_down_counter = 20

    def cooldown(self):

        if self.cool_down_counter > 0:
            self.cool_down_counter -= 1

    def move_lasers(self):

        for laser in self.lasers[:]:

            laser.move()

            if laser.off_screen():
                self.lasers.remove(laser)

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.ship_img.get_width(),
            self.ship_img.get_height()
        )

# =========================
# Player Ship Class
# =========================

class Player(Ship):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_type = PlayerLaser

        self.x_vel = 9

    def move_left(self):
        self.x -= self.x_vel

    def move_right(self):
        self.x += self.x_vel

    def shoot(self):

        if self.cool_down_counter == 0:

            laser = self.laser_type(
                self.x,
                self.y - self.ship_height,
            )

            self.lasers.append(laser)

            self.cool_down_counter = 10


# =========================
# Enemy Ship Class
# =========================

class Enemy(Ship):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.ship_img, self.laser_img = random.choice([
            (RED_SPACE_SHIP, RED_BULLET),
            (GREEN_SPACE_SHIP, GREEN_BULLET),
            (BLUE_SPACE_SHIP, BLUE_BULLET)
        ])

        self.laser_type = EnemyLaser

        # Enemy movement speed
        self.y_vel = random.randint(1, 3)

        # Random time before the first shot
        self.shoot_timer = random.randint(60, 180)

        self.health = 20

    def move(self):
        self.y += self.y_vel

    def shoot(self):

        if self.shoot_timer <= 0:

            laser = EnemyLaser(
                self.x + self.ship_width / 2,
                self.y + self.ship_height,
                self.laser_img
            )

            self.lasers.append(laser)

            self.shoot_timer = random.randint(60, 180)

    def update(self):

        self.move()

        self.shoot_timer -= 1

        self.shoot()

        self.cooldown()
        self.move_lasers()


def collide(obj1, obj2):
    return obj1.get_rect().colliderect(obj2.get_rect())

# =========================
# Main Game
# =========================

def main():

    spawn_timer = 0

    run = True

    level = 1
    lives = 5

    clock = pygame.time.Clock()

    # Create player
    ship = Player(
        WIDTH / 2,
        HEIGHT - 100
    )

    # Create enemies
    enemies = []

    for _ in range(5):

        x = random.randint(
            0,
            WIDTH - 50
        )

        y = random.randint(
            -500,
            -50
        )

        enemies.append(
            Enemy(x, y)
        )

    # =========================
    # Draw Window
    # =========================

    def redraw_window():

        # Background
        WIN.blit(
            BACKGROUND,
            (0, 0)
        )

        # Level text
        level_label = MAIN_FONT.render(
            f"Level: {level}",
            1,
            WHITE
        )

        # Lives text
        lives_label = MAIN_FONT.render(
            f"Lives: {lives}",
            1,
            WHITE
        )

        WIN.blit(
            level_label,
            (
                WIDTH - level_label.get_width() - 10,
                0
            )
        )

        WIN.blit(
            lives_label,
            (10, 0)
        )

        # Draw player
        ship.draw(WIN)

        # Draw enemies
        for enemy in enemies:
            enemy.draw(WIN)

        pygame.display.update()

    # =========================
    # Game Loop
    # =========================

    while run:

        # =========================
        # Spawn Enemies
        # =========================

        spawn_timer -= 1

        if spawn_timer <= 0:

            x = random.randint(0, WIDTH - 50)

            enemy = Enemy(
                x,
                -50
            )

            enemies.append(enemy)

            # Spawn another enemy in 1-3 seconds
            spawn_timer = random.randint(60, 180)

        clock.tick(FPS)

        # =========================
        # Events
        # =========================

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        # =========================
        # Player Movement
        # =========================

        keys = pygame.key.get_pressed()

        if (
            keys[pygame.K_a]
            or keys[pygame.K_LEFT]
        ) and ship.x - ship.x_vel >= 0:

            ship.move_left()

        if (
            keys[pygame.K_d]
            or keys[pygame.K_RIGHT]
        ) and ship.x + ship.x_vel <= WIDTH - ship.ship_width:

            ship.move_right()

        # =========================
        # Player Shooting
        # =========================

        if keys[pygame.K_SPACE]:
            ship.shoot()

        # =========================
        # Update Player
        # =========================

        ship.cooldown()
        ship.move_lasers()

        # =========================
        # Update Enemies
        # =========================

        for enemy in enemies[:]:

            enemy.update()

            # Enemy reached the bottom
            if enemy.y > HEIGHT:

                lives -= 1
                enemies.remove(enemy)

                if lives <= 0:
                    lose()
                    run = False

        # =========================
        # Player Lasers -> Enemies
        # =========================

        for laser in ship.lasers[:]:

            for enemy in enemies[:]:

                if collide(laser, enemy):

                    # Damage enemy
                    enemy.health -= laser.damage

                    # Remove the laser
                    ship.lasers.remove(laser)

                    # Destroy enemy if health reaches 0
                    if enemy.health <= 0:
                        enemies.remove(enemy)

                    break

        # =========================
        # Enemy Lasers -> Player
        # =========================

        for enemy in enemies:

            for laser in enemy.lasers[:]:

                if collide(laser, ship):

                    # Damage player
                    ship.health -= laser.damage

                    # Remove the laser
                    enemy.lasers.remove(laser)

                    break

        # =========================
        # Enemy Ships -> Player
        # =========================

        for enemy in enemies[:]:

            if collide(enemy, ship):

                # Damage player
                ship.health -= 25

                # Remove enemy after collision
                enemies.remove(enemy)

        # =========================
        # Player Health
        # =========================

        if ship.health <= 0:

            lives -= 1

            if lives <= 0:
                lose()
                run = False

            else:
                # Reset player's health
                ship.health = 100

        # =========================
        # Draw Everything
        # =========================

        redraw_window()


    pygame.quit()


# =========================
# Run Game
# =========================

if __name__ == "__main__":
    main()