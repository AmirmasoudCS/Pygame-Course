import pygame
pygame.font.init()

FONT = pygame.font.SysFont("arial", 60, bold=True)
FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
DARK_OVERLAY = (0, 0, 0, 80)


CROWN = pygame.transform.scale(pygame.image.load("./project_05/assets/crown.png"), (44, 25))

pygame.mixer.music("./project_05/assets/sounds/bg_music.mp3")
MOVE_SOUND = pygame.mixer.Sound("./project_05/assets/sounds/move.wav")
CAPTURE_SOUND = pygame.mixer.Sound("./project_05/assets/sounds/piece_capturing.wav")