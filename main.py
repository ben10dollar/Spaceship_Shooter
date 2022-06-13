import pygame, os

pygame.font.init()
pygame.mixer.init()
pygame.display.init()

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

# Assets
ORANGE_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'Orange_Spaceship.png'))
GREEN_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'Green_Spaceship.png'))
SPACE = pygame.image.load(os.path.join('Assets', 'Space_Background.jpg'))
# Assign game objects based on style
SHIP_1_IMG = ORANGE_SHIP_IMG
SHIP_2_IMG = GREEN_SHIP_IMG
BACKGROUND = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))

# Principal Functions
# https://realpython.com/lessons/using-blit-and-flip/
def draw_window():
    pass


# main Definition
def main():
    # Running Loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Update all parameters
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

# main Execution
main()