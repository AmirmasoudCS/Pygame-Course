import pygame
import random
import math
import time

pygame.init()
pygame.font.init()

FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4

RECT_HEIGHT, RECT_WIDTH = HEIGHT // ROWS, WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BG_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

FONT = pygame.font.SysFont("comicsans", 60, bold=True)

MOVE_VEL = 20 

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        return self.COLORS[int(math.log2(self.val)) - 1]

    def draw(self, win):
        color = self.get_color()
        pygame.draw.rect(win, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.val), 1, FONT_COLOR)
        win.blit(text, (self.x + (RECT_WIDTH / 2 - text.get_width() / 2), self.y + (RECT_HEIGHT / 2 - text.get_height() / 2)))


    def move(self, delta):
        pass

    def set_position(self):
        pass

def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

def draw(window, tiles):

    window.fill(BG_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)

    pygame.display.update()

def get_random_position(tiles):
    row, col = None, None
    while True:
        row, col = random.randrange(0, ROWS), random.randrange(0, COLS)
        if f"{row}{col}" not in tiles:
            break
    return row, col

def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()

    if direction == "left":
        sort_function = lambda x: x.col
        reversed = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col-1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
        ceil = True


    elif direction == "right":
        pass
    elif direction == "up":
        pass
    elif direction == "down":
        pass

    while updated:
        clock.tick(FPS)
        updated = False


def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_position(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)

    return tiles

def main(window):

    run = True
    clock = pygame.time.Clock()

    tiles = generate_tiles()

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, tiles)

    pygame.quit()

if __name__ == "__main__":
    main(WIN)