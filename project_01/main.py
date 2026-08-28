import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

BG = pygame.transform.scale(pygame.image.load("./project_01/space.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEGIHT = 60

PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "purple", player)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(WIDTH/2, HEIGHT - PLAYER_HEGIHT, PLAYER_WIDTH, PLAYER_HEGIHT)

    clock = pygame.time.Clock()

    while run:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        
        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()