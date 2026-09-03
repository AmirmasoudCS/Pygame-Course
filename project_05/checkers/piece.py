from project_05.checkers.constants import RED, WHITE

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.direction = 1 if self.color == WHITE else -1
        self.x = 0
        self.y = 0