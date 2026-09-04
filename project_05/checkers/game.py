import pygame
from project_05.checkers.board import Board
from project_05.checkers.constants import (
    RED,
    WHITE,
)

class Game:

    def __init__(self, win):
        self.win = win
        self.init()

    def update(self):
        self.board.draw(self.win)

        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()