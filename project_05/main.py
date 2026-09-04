import pygame
import time
from project_05.checkers.constants import (
    WIDTH,
    HEIGHT,
    FPS,
    SQUARE_SIZE,
    RED,
    FINISH,
)
from project_05.checkers.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def get_row_col_from_mouse(pos):
    x, y = pos
    row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
    return row, col

def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    winner = None

    pygame.mixer.music.set_volume(0.08)
    pygame.mixer.music.play(loops=-1)

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                #if game.turn == RED:
                game.select(row, col)

        if winner is None:
            winner = game.winner()
            if winner is not None:
                pygame.mixer.music.stop()
                FINISH.play()

        if winner is None:
            game.update()
        else:
            game.draw_winner(winner)
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
