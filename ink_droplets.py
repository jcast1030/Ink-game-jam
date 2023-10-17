import pygame

WIDTH = 40
HEIGHT = 40

class Drop:

    def __init__(self, speed, dposx, dposy):
        self.speed = speed
        self.position_x = dposx
        self.position_y = dposy
        self.color = "blue"
        print("drop created , ", speed)

    def show(self, screen):
         pygame.draw.rect(screen, "blue", pygame.Rect(self.position_x, self.position_y, WIDTH, HEIGHT))
