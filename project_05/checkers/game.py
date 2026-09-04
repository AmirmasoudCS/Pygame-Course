import pygame
from project_05.checkers.board import Board
from project_05.checkers.constants import (
    RED,
    WHITE,
    BLUE,
    SQUARE_SIZE,
    FONT,
    WIDTH, 
    HEIGHT,
    DARK_OVERLAY,
    MOVE_SOUND,
    CAPTURE_SOUND,
    KING,
)

class Game:

    def __init__(self, win):
        self.win = win
        self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)

        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()

    def draw_winner(self, winner):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill(DARK_OVERLAY)
        self.win.blit(overlay, (0, 0))

        winner_name = "Red" if winner == RED else "White"
        winner_color = RED if winner == RED else WHITE

        text = FONT.render(f"{winner_name} Wins!", True, winner_color)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.win.blit(text, text_rect)

        pygame.display.update()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            was_king = self.selected.king
            self.board.move(self.selected, row, col)
            MOVE_SOUND.play()
            if not was_king and self.selected.king:
                KING.play()
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
                CAPTURE_SOUND.play()
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = []
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        old_white_kings = self.board.white_kings
        self.board = board
        if self.board.white_kings > old_white_kings:
            KING.play()
        self.change_turn()
