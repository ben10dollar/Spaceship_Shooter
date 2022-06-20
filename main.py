import time

import pygame
from literals import *
from gameplay import *

pygame.mixer.init()
pygame.display.init()


# https://realpython.com/lessons/using-blit-and-flip/
# https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
def draw_window(p1_ship, p2_ship, p1_bullets: list[pygame.Rect], p2_bullets: list[pygame.Rect], p1_lives, p2_lives, tokens):
    WINDOW.blit(BACKGROUND, (0, 0))

    p1_health_text = HEALTH_FONT.render("Lives: " + str(p1_lives), 1, WHITE)
    p2_health_text = HEALTH_FONT.render("Lives: " + str(p2_lives), 1, WHITE)

    WINDOW.blit(p1_health_text, (10, 10))
    WINDOW.blit(p2_health_text, (WIDTH - 10 - p2_health_text.get_width(), 10))

    pygame.draw.rect(WINDOW, WHITE, CENTRAL_BARRIER)

    WINDOW.blit(SHIP_1_IMG, (p1_ship.x, p1_ship.y))
    WINDOW.blit(SHIP_2_IMG, (p2_ship.x, p2_ship.y))

    for bullet in p1_bullets:
        pygame.draw.rect(WINDOW, GREEN, bullet, border_radius=BULLET_BORDER_RADIUS)
    for bullet in p2_bullets:
        pygame.draw.rect(WINDOW, ORANGE, bullet, border_radius=BULLET_BORDER_RADIUS)

    for token in tokens:
        WINDOW.blit(RAPID_FIRE_TOKEN, (token.x, token.y))

    pygame.display.flip()
    pygame.display.update()


# main Definition
def main():
    # Define ships
    p1_ship = pygame.Rect(WIDTH // 4, HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    p2_ship = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Define bullets
    p1_bullets = []
    p2_bullets = []
    p1_last_fire = 0
    p2_last_fire = 0

    # Define lives
    p1_lives = STARTING_LIVES
    p2_lives = STARTING_LIVES

    # Define fire interval
    p1_max_bullets = MAX_BULLETS
    p2_max_bullets = MAX_BULLETS
    p1_power_up_start = 0
    p2_power_up_start = 0

    # Tokens
    tokens = []
    create_token(tokens, HEIGHT//2 - TOKEN_HEIGHT//2)

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

        # Consolidate all key inputs into keys_pressed list
        keys_pressed = pygame.key.get_pressed()

        # Handle spaceships
        move_spaceships(p1_ship, p2_ship, keys_pressed)

        # Check and moderate bullet creation
        if pygame.time.get_ticks() - p1_last_fire >= FIRE_INTERVAL:
            p1_last_fire = p1_create_bullets(p1_bullets, p1_ship, p1_max_bullets, keys_pressed)
        if pygame.time.get_ticks() - p2_last_fire >= FIRE_INTERVAL:
            p2_last_fire = p2_create_bullets(p2_bullets, p2_ship, p2_max_bullets, keys_pressed)

        # if pygame.time.get_ticks()

        for token in tokens:
            if check_collision(p1_ship, token):
                p1_power_up_start = pygame.time.get_ticks()
                p1_max_bullets *= 2
                tokens.remove(token)
            if check_collision(p2_ship, token):
                p2_power_up_start = pygame.time.get_ticks()
                p2_max_bullets *= 2
                tokens.remove(token)

        if pygame.time.get_ticks() - p1_power_up_start == POWER_UP_DURATION:
            p1_max_bullets = MAX_BULLETS
        if pygame.time.get_ticks() - p2_power_up_start == POWER_UP_DURATION:
            p1_max_bullets = MAX_BULLETS

        for bullet in p1_bullets:
            if check_collision(bullet, p2_ship):
                p1_bullets.remove(bullet)
                p2_lives -= 1
            elif check_collision(bullet, [WIDTH, WIDTH * 2]):
                p1_bullets.remove(bullet)
            else:
                bullet.x += BULLET_VEL
        for bullet in p2_bullets:
            if check_collision(bullet, p1_ship):
                p2_bullets.remove(bullet)
                p1_lives -= 1
            elif check_collision(bullet, [-WIDTH, 0]):
                p2_bullets.remove(bullet)
            else:
                bullet.x -= BULLET_VEL

        if p1_lives == 0:
            draw_winner("Player 1 Wins!")
            break
        elif p2_lives == 0:
            draw_winner("Player 2 Wins!")
            break

        draw_window(p1_ship, p2_ship, p1_bullets, p2_bullets, p1_lives, p2_lives, tokens)


# main Execution
main()
