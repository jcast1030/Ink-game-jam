import pygame
import random
from ink_droplets import Drop
from player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

rect = pygame.Rect(5,5,5,5)

# Drop(5, random.randint(0, 1280), random.randint(0, 720))

player = Player(screen.get_width() / 2, screen.get_height() / 2)
drops = []


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    player.show(screen)


    for drop in drops:
        drop.show(screen)
        drop.position_y = drop.position_y + drop.speed * dt
    #for drop in drops:
      #  if rect.colliderect(drop):
     #       drop.color = "red"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        drops.append(Drop(random.randint(5, 50), random.randint(
            0, 1280), random.randint(-20, 0)))
    if keys[pygame.K_w]:
        player.position_y -= 300 * dt
    if keys[pygame.K_s]:
        player.position_y += 300 * dt
    if keys[pygame.K_a]:
        player.position_x -= 300 * dt
    if keys[pygame.K_d]:
        player.position_x += 300 * dt

    # flip() the display to put your work on screens

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

    dt = clock.tick(60) / 1000


pygame.quit()
