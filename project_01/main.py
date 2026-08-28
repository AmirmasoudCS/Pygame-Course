import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

BG = pygame.transform.scale(pygame.image.load("./project_01/space.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEGIHT = 60

PLAYER_VEL = 5

FONT = pygame.font.SysFont("cosmicsans", 30)

def draw(player, elapsed_time):

    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")

    WIN.blit(time_text, (10,10))

    pygame.draw.rect(WIN, "purple", player)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(WIDTH/2, HEIGHT - PLAYER_HEGIHT, PLAYER_WIDTH, PLAYER_HEGIHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    while run:

        clock.tick(60)

        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        
        draw(player, elapsed_time)

    pygame.quit()

if __name__ == "__main__":
    main()