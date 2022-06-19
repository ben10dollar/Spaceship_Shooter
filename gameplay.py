import pygame
from literals import *


def move_spaceships(p1_ship, p2_ship, keys_pressed: list):
    # Move spaceship 1
    if keys_pressed[pygame.K_s] and p1_ship.y + p1_ship.height < HEIGHT:
        p1_ship.y += VEL
    if keys_pressed[pygame.K_w] and p1_ship.y > 0:
        p1_ship.y -= VEL
    if keys_pressed[pygame.K_d] and p1_ship.x + p1_ship.width < WIDTH:
        p1_ship.x += VEL
    if keys_pressed[pygame.K_a] and p1_ship.x > 0:
        p1_ship.x -= VEL

    # Move spaceship 2
    if keys_pressed[pygame.K_DOWN] and p2_ship.y + p2_ship.height < HEIGHT:
        p2_ship.y += VEL
    if keys_pressed[pygame.K_UP] and p2_ship.y > 0:
        p2_ship.y -= VEL
    if keys_pressed[pygame.K_RIGHT] and p2_ship.x + p2_ship.width < WIDTH:
        p2_ship.x += VEL
    if keys_pressed[pygame.K_LEFT] and p2_ship.x > 0:
        p2_ship.x -= VEL


# Returns time of firing if successful; if unsuccessful, returns 0
def p1_create_bullets(p1_bullets: list[pygame.Rect], p1_ship, keys_pressed: list):
    # If the max bullets aren't already reached, create a bullet at the middle of the aircraft
    if keys_pressed[pygame.K_SPACE] and len(p1_bullets) < MAX_BULLETS:
        p1_bullets.append(
            pygame.Rect(
                p1_ship.x + p1_ship.width, p1_ship.y + p1_ship.height // 2, BULLET_WIDTH, BULLET_HEIGHT))
        return pygame.time.get_ticks()
    return 0


# Returns time of firing if successful; if unsuccessful, returns 0
def p2_create_bullets(p2_bullets: list[pygame.Rect], p2_ship, keys_pressed: list):
    if keys_pressed[pygame.K_RCTRL] and len(p2_bullets) < MAX_BULLETS:
        p2_bullets.append(
            pygame.Rect(
                p2_ship.x, p2_ship.y + p2_ship.height // 2, BULLET_WIDTH, BULLET_HEIGHT))
        return pygame.time.get_ticks()
    return 0


def check_collision(collider: pygame.Rect, boundary):
    if type(boundary) == pygame.Rect:
        # If x-coordinates match up
        if boundary.x <= collider.x <= boundary.x + boundary.width \
                or boundary.x <= collider.x + collider.width <= boundary.x + boundary.width:
            # If y-coordinates match up
            if boundary.y <= collider.y <= boundary.y + boundary.height \
                    or boundary.y <= collider.y + collider.height <= boundary.y + boundary.height:
                return True
    elif type(boundary) == list:
        if boundary[0] <= collider.x <= boundary[1] \
                or boundary[0] <= collider.x + collider.width <= boundary[1]:
            return True
    return False


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WINDOW.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)