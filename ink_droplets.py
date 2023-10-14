import pygame

class Drop:

    def __init__(self, speed, dposx, dposy):
        self.speed = speed
        self.position_x = dposx
        self.position_y = dposy
        print("drop created , ", speed)

    def show(self, screen):
        pygame.draw.circle(screen, "black", pygame.Vector2(
            self.position_x, self.position_y), 20)
