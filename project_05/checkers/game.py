import pygame
from project_05.checkers.board import Board
from project_05.checkers.constants import (
    RED,
    WHITE,
)

class Game:

    def __init__(self, win):
        self.win = win
        self._init()

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

    def select(self, row, col):
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.selecte(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        pass