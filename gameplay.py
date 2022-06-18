import pygame
from literals import *


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
        if boundary.x <= collider.x <= boundary.x + boundary.width:
            if boundary.y <= collider.y <= boundary.y + boundary.height:
                return True
            elif boundary.y <= collider.y + collider.height <= boundary.y + boundary.height:
                return True
    elif type(boundary) == int:
        if collider.x == boundary:
            return True
        elif collider.x + collider.width == boundary:
            return True
    return False


# def move_bullets(p1_bullets: list[pygame.Rect], p2_lives: int, p2_bullets: list[pygame.Rect]):
#     for bullet in p1_bullets:
#         if bullet.x > WIDTH - BULLET_WIDTH:
#             p1_bullets.remove(bullet)
#         elif check_collision(bullet, p2_ship):
#             p1_bullets.remove(bullet)
#             p2_lives.
#         else:
#             bullet.x += BULLET_VEL
#     for bullet in p2_bullets:
#         if bullet.x > 0:
#             bullet.x -= BULLET_VEL
#         else:
#             p2_bullets.remove(bullet)
#
# def move_bullet(bullet: pygame.Rect):
#     bullet.x =
