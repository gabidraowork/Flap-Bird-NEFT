import config
from sys import exit
import pygame
import components
from population import Population
from player import Player

pygame.init()
clock = pygame.time.Clock()
population = Population(config.population_size)
population.start_population()

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

def main():
    pipes_spawn_time = 0
    while True:
        quit_game()

        config.window.fill((0,0,0))

        # spawna o châo

        config.ground.draw(config.window)


        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 100
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)

        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            population.natural_selection()
            pipes_spawn_time = 0
        
        clock.tick(60)
        pygame.display.flip()

main()

