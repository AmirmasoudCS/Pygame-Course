import pygame
from project_05.checkers.board import Board
from project_05.checkers.constants import (
    RED,
    WHITE,
    BLUE,
    SQUARE_SIZE,
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
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = moves
            pygame.draw.circle(self.win, BLUE, (row * SQUARE_SIZE - SQUARE_SIZE // 2, col * SQUARE_SIZE - SQUARE_SIZE // 2), 15)

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
