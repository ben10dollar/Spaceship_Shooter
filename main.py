import pygame, os

pygame.font.init()
pygame.mixer.init()

# Window/Screen
# https://stackoverflow.com/questions/6104207/what-exactly-does-pygame-display-set-mode-do
WIDTH, HEIGHT = 1200, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shooter!")
BARR_WIDTH = 5
CENTRAL_BARRIER = pygame.Rect(WIDTH//2 - BARR_WIDTH//2, 0, BARR_WIDTH, HEIGHT)

# Colors
WHITE = (255, 255, 255)
ORANGE = ()
GREEN = ()
BLACK = (0, 0, 0)

# Text
HEALTH_FONT = pygame.font.SysFont('verdana', 50)
WINNER_FONT = pygame.font.SysFont('verdana', 125)

# Game Settings
FPS = 60
VEL = 5
BULLET_VEL = 8
MAX_BULLETS = 3
STARTING_LIVES = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# User Events
SHIP_1_HIT = pygame.USEREVENT + 1
SHIP_2_HIT = pygame.USEREVENT + 2
