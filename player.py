import random
import pygame
import config
from brain import Brain
import numpy as np

class Player:
    size = 20
    gravity = 2.2
    dt = 0.1
    def __init__(self):
        #Bird
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, Player.size, Player.size)
        self.color = random.randint(100,255),random.randint(100,255),random.randint(100,255)
        self.vel = 0
        self.flap = False
        self.alive = True
        self.lifespan = 0

        #AI
        self.decision = None
       
        self.fitness = 0
        self.vision = [0, 0, 0, 0]
        self.inputs = len(self.vision) + 1
        self.brain = Brain(self.inputs)
        self.brain.generate_network()

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)

    def sky_collision(self):
        return bool(self.rect.y < 30)

    def pipe_collision(self):
        for p in config.pipes:
            if (self.rect.colliderect(p.rect_u) or
                self.rect.colliderect(p.rect_b)):
                return True

        return False


    def update(self, ground):
        if self.vel >= -6:
            self.flap = False

        if not (self.ground_collision(ground) or self.pipe_collision()):
            #Gravity
            self.vel += Player.gravity * Player.dt
            self.rect.y += self.vel
            if self.vel >= 10:
                self.vel = 10

            self.lifespan += 1
        else:
            self.alive = False
            self.flap = False
            self.vel = 0

    def bird_flap(self):
        if not self.flap and not self.sky_collision():
            self.flap = True
            self.vel = -5

    @staticmethod
    def closest_pipe():
        for p in config.pipes:
            if not p.passed:
                return p

    def look(self):
        if not config.pipes:
            return

        pipe = self.closest_pipe()

        if pipe is None:
            return

        # Distância até o cano superior
        dist_u = np.sqrt(
            (self.rect.centerx - pipe.rect_u.bottomleft[0])**2 +
            (self.rect.centery - pipe.rect_u.bottomleft[1])**2
        )
        pygame.draw.line(config.window, self.color, self.rect.center, pipe.rect_u.bottomleft)


        # Distância até o cano inferior
        dist_b = np.sqrt(
            (self.rect.centerx - pipe.rect_b.topleft[0])**2 +
            (self.rect.centery - pipe.rect_b.topleft[1])**2
        )
        pygame.draw.line(config.window, self.color, self.rect.center, pipe.rect_b.topleft)
        # Distância até o chão
        dist_g = config.ground.y - self.rect.bottom
        pygame.draw.line(config.window, self.color, self.rect.center, (50 + Player.size/2, config.ground.y))


        self.vision[0] = dist_u / 500
        self.vision[1] = dist_b / 500
        self.vision[2] = dist_g / 500
        self.vision[3] = self.vel / 10
        


    #Ai related functions
    def think(self):
        self.decision = self.brain.feed_foward(self.vision)
        if self.decision >= 0.75:
            self.bird_flap()

    def calculate_fitness(self):
        self.fitness = self.lifespan

    def clone(self):
        clone = Player()
        clone.brain = self.brain.clone()
        clone.vision = self.vision

        clone.fitness = 0 
        clone.lifespan = 0
        return clone

    
           
        
