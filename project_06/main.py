import pygame
import time

pygame.init()


BLACK = (0, 0, 0)

FPS = 60


WIDTH, HEIGHT = 700, 500

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 70

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


class Paddle:

    COLOR = (255, 255, 255)

    def __init__(self, x, y, width=PADDLE_WIDTH, height=PADDLE_HEIGHT):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 3

    def draw(self, win):

        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=False, down=False):
        if up and self.y - self.velocity > 0:
            self.y -= self.velocity
        if down and self.y + self.velocity + self.height < HEIGHT:
            self.y += self.velocity

def draw(win, l_paddle, r_paddle):

    win.fill(BLACK)

    l_paddle.draw(win)
    r_paddle.draw(win)

    pygame.display.update()


def main():

    run = True

    clock = pygame.time.Clock()


    left_paddle = Paddle(0, HEIGHT//2 - PADDLE_HEIGHT//2)
    right_paddle = Paddle(WIDTH - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2)


    while run:

        clock.tick(FPS)

        draw(WIN, left_paddle, right_paddle)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move(up=True)
        if keys[pygame.K_s]:
            left_paddle.move(down=True)
        if keys[pygame.K_UP]:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN]:
            right_paddle.move(down=True)

    pygame.quit()


if __name__ == "__main__":

    main()
