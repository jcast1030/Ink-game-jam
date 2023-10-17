import pygame

WIDTH = 80
HEIGHT = 80


class Player:
    def __init__(self, dposx, dposy):
        self.position_x = dposx
        self.position_y = dposy
        self.rect = pygame.Rect(self.position_x, self.position_y, WIDTH, HEIGHT)
        print("player created ")

    def show(self, screen):
        pygame.draw.rect(screen, "green", self.rect)