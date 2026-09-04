import pygame
from project_05.checkers.board import Board
from project_05.checkers.constants import (
    RED,
    WHITE,
)

class Game:

    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.win = win
    