import pygame
import time
from project_05.checkers.constants import (
    WIDTH,
    HEIGHT,
    FPS,
)
from project_05.checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def main():

    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.create_board()

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)

        pygame.display.update()

    pygame.quit()
    
if __name__ == "__main__":
    main()
