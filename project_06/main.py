import pygame
import time

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60


WIDTH, HEIGHT = 700, 500

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 70

BALL_RADIUS = 7
BALL_VELOCITY = 4

DASH_WIDTH, DASH_HEIGHT = 4, 10
DASH_GAP = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

class Ball:

    COLOR = WHITE

    def __init__(self, x=WIDTH//2-BALL_RADIUS//2, y=HEIGHT//2-BALL_RADIUS//2, radius=BALL_RADIUS, velocity=BALL_VELOCITY):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = velocity
        self.y_velocity = velocity

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
class Paddle:

    COLOR = WHITE

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

    for i in range(0, HEIGHT, DASH_HEIGHT + DASH_GAP):
        pygame.draw.rect(win, WHITE, (WIDTH//2-DASH_WIDTH, i, DASH_WIDTH, DASH_HEIGHT))

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
