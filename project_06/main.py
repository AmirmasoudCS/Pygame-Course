import pygame
pygame.init()
import time

BLACK = (0, 0, 0)
FPS = 60

WIDTH, HEIGHT = 700, 500
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 70
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

class Paddle:
    COLOR = WHITE = (255, 255, 255)
    def __init__(self, x, y, width=PADDLE_WIDTH, height=PADDLE_HEIGHT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

def draw(win, l_paddle, r_paddle):
    win.blit(BLACK)
    pygame.draw.rect(l_paddle)
    pygame.draw.rect(r_paddle)
    pygame.display.update()

def main():

    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(0, HEIGHT//2 - PADDLE_HEIGHT//2)
    right_paddle = Paddle(WIDTH - PADDLE_WIDTH, HEIGHT//2-PADDLE_HEIGHT//2)

    while run:
        clock.tick(FPS)
        draw(WIN, left_paddle, right_paddle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()


if __name__ == "__main__":
    main()