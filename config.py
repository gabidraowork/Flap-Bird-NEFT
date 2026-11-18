import pygame
import components

win_height = 720
win_width = 550
window = pygame.display.set_mode((win_width, win_height))

population_size = 200

ground = components.Ground(win_width)

pipes = []