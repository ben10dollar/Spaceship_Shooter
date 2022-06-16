import time

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
FIRE_INTERVAL = 1000
STARTING_LIVES = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 133, 100

# User Events
SHIP_1_HIT = pygame.USEREVENT + 1
SHIP_2_HIT = pygame.USEREVENT + 2

# Time Limits


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
def draw_window(p1_ship, p2_ship, p1_bullets: list[pygame.Rect], p2_bullets: list[pygame.Rect], p1_lives, p2_lives):
    WINDOW.blit(BACKGROUND, (0, 0))

    p1_health_text = HEALTH_FONT.render("Lives: " + str(p1_lives), 1, WHITE)
    p2_health_text = HEALTH_FONT.render("Lives: " + str(p2_lives), 1, WHITE)

    WINDOW.blit(p1_health_text, (10, 10))
    WINDOW.blit(p2_health_text, (WIDTH - 10 - p2_health_text.get_width(), 10))

    WINDOW.blit(SHIP_1_IMG, (p1_ship.x, p1_ship.y))
    WINDOW.blit(SHIP_2_IMG, (p2_ship.x, p2_ship.y))

    for bullet in p1_bullets:
        pygame.draw.rect(WINDOW, GREEN, bullet, border_radius=BULLET_BORDER_RADIUS)
    for bullet in p2_bullets:
        pygame.draw.rect(WINDOW, ORANGE, bullet, border_radius=BULLET_BORDER_RADIUS)

    pygame.display.flip()
    pygame.display.update()


def move_spaceships(p1_ship, p2_ship, keys_pressed: list):
    # Move spaceship 1
    if keys_pressed[pygame.K_s] and p1_ship.y + p1_ship.width < HEIGHT:
        p1_ship.y += VEL
    if keys_pressed[pygame.K_w] and p1_ship.y > 0:
        p1_ship.y -= VEL
    if keys_pressed[pygame.K_d] and p1_ship.x + p1_ship.height < WIDTH:
        p1_ship.x += VEL
    if keys_pressed[pygame.K_a] and p1_ship.x > 0:
        p1_ship.x -= VEL

    # Move spaceship 2
    if keys_pressed[pygame.K_DOWN] and p2_ship.y + p2_ship.width < HEIGHT:
        p2_ship.y += VEL
    if keys_pressed[pygame.K_UP] and p2_ship.y > 0:
        p2_ship.y -= VEL
    if keys_pressed[pygame.K_RIGHT] and p2_ship.x + p2_ship.height < WIDTH:
        p2_ship.x += VEL
    if keys_pressed[pygame.K_LEFT] and p2_ship.x > 0:
        p2_ship.x -= VEL


def p1_create_bullets(p1_bullets: list[pygame.Rect], p1_last_fire, p1_ship, keys_pressed: list):
    # If the max bullets aren't already reached, create a bullet at the middle of the aircraft
    if keys_pressed[pygame.K_LCTRL] and p1_last_fire - time.clock() > FIRE_INTERVAL and len(p1_bullets) < MAX_BULLETS:
        p1_bullets.append(
            pygame.Rect(
                p1_ship.x + p1_ship.width, p1_ship.y + p1_ship.height // 2, BULLET_WIDTH, BULLET_HEIGHT))
        p1_last_fire = time.clock()


def p2_create_bullets(p2_bullets: list[pygame.Rect], p2_ship, keys_pressed: list):
    if keys_pressed[pygame.K_RCTRL] and len(p2_bullets) < MAX_BULLETS:
        p2_bullets.append(
            pygame.Rect(
                p2_ship.x, p2_ship.y + p2_ship.height // 2, BULLET_WIDTH, BULLET_HEIGHT))


def move_bullets(p1_bullets: list[pygame.Rect], p2_bullets: list[pygame.Rect]):
    for bullet in p1_bullets:
        if bullet.x < WIDTH - BULLET_WIDTH:
            bullet.x += BULLET_VEL
        else:
            p1_bullets.pop()
    for bullet in p2_bullets:
        if bullet.x > 0:
            bullet.x -= BULLET_VEL
        else:
            p2_bullets.pop()


# main Definition
def main():
    # Define ships
    p1_ship = pygame.Rect(WIDTH // 4, HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    p2_ship = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Define bullets
    p1_bullets = []
    p2_bullets = []
    p1_last_fire = 0

    # Define lives
    p1_lives = STARTING_LIVES
    p2_lives = STARTING_LIVES

    # Running Loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Loop will run FPS times per second
        clock.tick(FPS)
        # Update all parameters
        for event in pygame.event.get():
            # Allows Spaceship_Shooter's termination
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()

        # Handle spaceships
        move_spaceships(p1_ship, p2_ship, keys_pressed)

        p1_create_bullets(p1_bullets, p1_ship, keys_pressed)
        move_bullets(p1_bullets, p2_bullets)

        draw_window(p1_ship, p2_ship, p1_bullets, p2_bullets, p1_lives, p2_lives)


# main Execution
main()
