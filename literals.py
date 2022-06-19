import os
import pygame


pygame.font.init()


# Window/Screen
# https://stackoverflow.com/questions/6104207/what-exactly-does-pygame-display-set-mode-do
WIDTH, HEIGHT = 1200, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shooter!")
BARR_WIDTH = 5
CENTRAL_BARRIER = pygame.Rect(WIDTH // 2 - BARR_WIDTH // 2, 0, BARR_WIDTH, HEIGHT)

# Colors
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Text
HEALTH_FONT = pygame.font.SysFont('verdana', 50)
WINNER_FONT = pygame.font.SysFont('verdana', 125)

# Gameplay Settings
FPS = 60
VEL = 5
BULLET_VEL = 8
MAX_BULLETS = 3
BULLET_HEIGHT = 10
BULLET_WIDTH = 30
BULLET_BORDER_RADIUS = 3
# In milliseconds (ms)
FIRE_INTERVAL = 500
STARTING_LIVES = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 133

# User Events
SHIP_1_HIT = pygame.USEREVENT + 1
SHIP_2_HIT = pygame.USEREVENT + 2

# Assets
ORANGE_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'Orange_Spaceship.png'))
GREEN_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'Green_Spaceship.png'))
SPACE = pygame.image.load(os.path.join('Assets', 'Space_Background.jpg'))
# Assign game objects based on style
SHIP_1_IMG = pygame.transform.scale(
    pygame.transform.rotate(
        GREEN_SHIP_IMG, -90), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
SHIP_2_IMG = pygame.transform.scale(
    pygame.transform.rotate(
        ORANGE_SHIP_IMG, 90), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
BACKGROUND = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))
