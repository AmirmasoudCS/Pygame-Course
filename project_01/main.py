import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

BG = pygame.transform.scale(pygame.image.load("./project_01/space.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEGIHT = 60

PLAYER_VEL = 3.5

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "purple", player)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(WIDTH/2, HEIGHT - PLAYER_HEGIHT, PLAYER_WIDTH, PLAYER_HEGIHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += PLAYER_VEL
        
        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()