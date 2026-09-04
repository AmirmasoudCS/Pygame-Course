import pygame
pygame.init()
import time

BLACK = (0, 0, 0)
FPS = 60

WIDTH, HEIGHT = 700, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

def draw(win):
    win.blit(BLACK)

    pygame.display.update()

def main():

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()


if __name__ == "__main__":
    main()