import pygame
import random

class Ground:
    ground_level = 500

    def __init__(self, win_width):
        self.x, self.y = 0, Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, win_width,5)

    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), self.rect)


class Pipes:
    ground_level = 500
    width = 15
    opening = 100

    def __init__(self, win_width):
        self.x, self.y = win_width - 30, random.randint(20, self.ground_level - 20)
        self.passed = False
        self.off_screen = False
       

    def draw(self, window):
        self.rect_u = pygame.Rect(self.x, 0, Pipes.width, self.y - Pipes.opening/2)
        self.rect_b = pygame.Rect(self.x, self.y + Pipes.opening/2, Pipes.width, self.ground_level - (self.y + Pipes.opening/2) )

        pygame.draw.rect(window, (255,255,255), self.rect_u)
        pygame.draw.rect(window, (255,255,255), self.rect_b)

    def update(self):
        self.x -= 2
        if self.x + Pipes.width <= 50:
            self.passed = True
        if self.x <= -self.width:
            self.off_screen = True