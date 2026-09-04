import pygame
import time

pygame.init()
pygame.font.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60

FONT = pygame.font.SysFont("comicsans", 50)

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

    def __init__(self, x=WIDTH//2, y=HEIGHT//2, radius=BALL_RADIUS, velocity=BALL_VELOCITY):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = velocity
        self.y_velocity = velocity

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self, left_paddle, right_paddle):

        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.y - self.radius <= 0:
            self.y_velocity *= -1

        if self.y + self.radius >= HEIGHT:
            self.y_velocity *= -1

        rect = self.get_rect()
        if rect.colliderect(left_paddle.get_rect()):
            self.x_velocity *= -1
        if rect.colliderect(right_paddle.get_rect()):
            self.x_velocity *= -1

    def reset(self):

        self.x = WIDTH//2
        self.y = HEIGHT//2

        self.x_velocity = BALL_VELOCITY
        self.y_velocity = BALL_VELOCITY

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
class Paddle:

    COLOR = WHITE

    def __init__(self, x, y, width=PADDLE_WIDTH, height=PADDLE_HEIGHT):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 4

    def draw(self, win):

        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=False, down=False):
        if up and self.y - self.velocity > 0:
            self.y -= self.velocity
        if down and self.y + self.velocity + self.height < HEIGHT:
            self.y += self.velocity

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

def draw(win, l_paddle, r_paddle, ball, left_score, right_score):

    win.fill(BLACK)

    for i in range(0, HEIGHT, DASH_HEIGHT + DASH_GAP):
        pygame.draw.rect(win, WHITE, (WIDTH//2-DASH_WIDTH, i, DASH_WIDTH, DASH_HEIGHT))

    l_paddle.draw(win)
    r_paddle.draw(win)
    ball.draw(win)

    left_score_text = FONT.render(str(left_score), 1, WHITE)
    right_score_text = FONT.render(str(right_score), 1, WHITE)

    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH*3//4 - right_score_text.get_width()//2, 20))

    pygame.display.update()


def main():

    run = True

    clock = pygame.time.Clock()


    left_paddle = Paddle(0, HEIGHT//2 - PADDLE_HEIGHT//2)
    right_paddle = Paddle(WIDTH - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2)

    ball = Ball()

    left_score = 0
    right_score = 0

    while run:

        clock.tick(FPS)

        ball.move(left_paddle, right_paddle)

        if ball.x - ball.radius <= 0:
            right_score += 1
            ball.reset()

        if ball.x + ball.radius >= WIDTH:
            left_score += 1
            ball.reset()

        draw(WIN, left_paddle, right_paddle, ball, left_score, right_score)


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
