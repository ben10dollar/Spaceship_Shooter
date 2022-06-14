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
CENTRAL_BARRIER = pygame.Rect(WIDTH // 2 - BARR_WIDTH // 2, 0, BARR_WIDTH, HEIGHT)

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
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 133, 100

# User Events
SHIP_1_HIT = pygame.USEREVENT + 1
SHIP_2_HIT = pygame.USEREVENT + 2

# Assets
ORANGE_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'Orange_Spaceship.png'))
GREEN_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'Green_Spaceship.png'))
SPACE = pygame.image.load(os.path.join('Assets', 'Space_Background.jpg'))
# Assign game objects based on style
SHIP_1_IMG = pygame.transform.rotate(
    pygame.transform.scale(
        GREEN_SHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)
SHIP_2_IMG = pygame.transform.rotate(
    pygame.transform.scale(
        ORANGE_SHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
BACKGROUND = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))


# Principal Functions
# https://realpython.com/lessons/using-blit-and-flip/
# https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
def draw_window(p1_ship, p2_ship, p1_lives, p2_lives):
    WINDOW.blit(BACKGROUND, (0, 0))

    p1_health_text = HEALTH_FONT.render("Lives: " + str(p1_lives), 1, WHITE)
    p2_health_text = HEALTH_FONT.render("Lives: " + str(p2_lives), 1, WHITE)

    WINDOW.blit(p1_health_text, (10, 10))
    WINDOW.blit(p2_health_text, (WIDTH-10, 10))

    WINDOW.blit(SHIP_1_IMG, (p1_ship.x, p1_ship.y))
    WINDOW.blit(SHIP_2_IMG, (p2_ship.x, p2_ship.y))

    pygame.display.update()


def move_spaceships(p1_ship, p2_ship, keys_pressed: list):
    for key_pressed in keys_pressed:
        match key_pressed:
            # Move spaceship 1
            case pygame.K_w:
                p1_ship.y += VEL
            case pygame.K_s:
                p1_ship.y -= VEL
            case pygame.K_d:
                p1_ship.x += VEL
            case pygame.K_a:
                p1_ship.x -= VEL

            # Move spaceship 2
            case pygame.K_UP:
                p2_ship.y += VEL
            case pygame.K_DOWN:
                p2_ship.y -= VEL
            case pygame.K_RIGHT:
                p2_ship.x += VEL
            case pygame.K_LEFT:
                p2_ship.x -= VEL


# main Definition
def main():
    # Define ships
    p1_ship = pygame.Rect(WIDTH // 4, HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    p2_ship = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Define bullets
    p1_bullets = []
    p2_bullets = []

    # Define lives
    p1_lives = STARTING_LIVES
    p2_lives = STARTING_LIVES

    # Running Loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Update all parameters
        clock.tick(FPS)
        for event in pygame.event.get():
            # Allows Spaceship_Shooter's termination
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        move_spaceships(p1_ship, p2_ship, keys_pressed)

        draw_window(p1_ship, p2_ship, p1_lives, p2_lives)

# main Execution
main()
