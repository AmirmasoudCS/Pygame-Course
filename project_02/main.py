import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle Ship")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_VEL = 7
MAX_BULLETS = 3

SHIPS_WIDTH = 55
SHIPS_HEIGT = 40
SHIPS_X_VEL = 5
SHIPS_Y_VEL = 3

YELLOW_SPACESHIP = pygame.image.load("./project_02/assets/spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP, (SHIPS_WIDTH, SHIPS_HEIGT)), 90)
YELLOW_SPACESHIP_X = WIDTH/4
YELLOW_SPACESHIP_Y = HEIGHT/2
YELLOW_HIT = pygame.USEREVENT + 1


RED_SPACESHIP = pygame.image.load("./project_02/assets/spaceship_red.png")
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP, (SHIPS_WIDTH, SHIPS_HEIGT)), 270)
RED_SPACESHIP_X = WIDTH-WIDTH/4
RED_SPACESHIP_Y = HEIGHT/2
RED_HIT = pygame.USEREVENT + 2


def handle_bullets(yellow_bullets, red_bullets, yellow, red):

    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x < 0:
            red_bullets.remove(bullet)

def draw(yellow, red, yellow_bullets, red_bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update()

def main():

    yellow_bullets = []
    red_bullets = []

    yellow = pygame.Rect(YELLOW_SPACESHIP_X, YELLOW_SPACESHIP_Y, SHIPS_WIDTH, SHIPS_HEIGT)
    red = pygame.Rect(RED_SPACESHIP_X, RED_SPACESHIP_Y, SHIPS_WIDTH, SHIPS_HEIGT)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+SHIPS_WIDTH, yellow.y + SHIPS_HEIGT//2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + SHIPS_HEIGT//2, 10, 5)
                    red_bullets.append(bullet)


        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] and yellow.x - SHIPS_X_VEL >= 0: # yellow left
            yellow.x -= SHIPS_X_VEL
        if keys_pressed[pygame.K_d] and yellow.x + SHIPS_X_VEL <= (WIDTH / 2) - SHIPS_WIDTH + 15: # yellow right
            yellow.x += SHIPS_X_VEL
        if keys_pressed[pygame.K_w] and yellow.y - SHIPS_Y_VEL >= 0: # yellow up
            yellow.y -= SHIPS_Y_VEL
        if keys_pressed[pygame.K_s] and yellow.y + SHIPS_Y_VEL <= HEIGHT - (SHIPS_HEIGT + 10): # yellow down
            yellow.y += SHIPS_Y_VEL

        if keys_pressed[pygame.K_LEFT] and red.x - SHIPS_X_VEL >= WIDTH / 2: # red left
            red.x -= SHIPS_X_VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + SHIPS_X_VEL <= WIDTH - (SHIPS_WIDTH - 15)  : # red right
            red.x += SHIPS_X_VEL
        if keys_pressed[pygame.K_UP] and red.y - SHIPS_Y_VEL >= 0: # red up
            red.y -= SHIPS_Y_VEL
        if keys_pressed[pygame.K_DOWN] and red.y + SHIPS_Y_VEL <= HEIGHT - (SHIPS_HEIGT + 10): # red down
            red.y += SHIPS_Y_VEL

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        draw(yellow, red)

    pygame.quit()

if __name__ == "__main__":
    main()