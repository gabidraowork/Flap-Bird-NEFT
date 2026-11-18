import operator
import random
import numpy as np
from player import Player
from brain import Brain
from NN.dense import Dense

class Species:
    def __init__(self, player : Player):
        self.players = []
        self.average_fitness = 0
        self.threshold = 1.2
        self.players.append(player)
        self.benchmark_fitness = player.fitness
        self.benchmark_brain = player.brain.clone()
        self.champion = player.clone()
        self.staleness = 0

    def similarity(self, brain : Brain):
        similarity = Species.weight_difference(self.benchmark_brain, brain)
        return self.threshold > similarity

    @staticmethod
    def weight_difference(brain_1: Brain, brain_2: Brain):
        total_weight_difference =  0 

        for l_1, l_2 in zip(brain_1.network, brain_2.network):
            if isinstance(l_1, Dense) and isinstance(l_2, Dense):
                total_weight_difference += np.sum(abs(l_1.weights - l_2.weights))

        return total_weight_difference
    
    def add_to_species(self, player : Player):
        self.players.append(player)

    def sort_players_by_fitness(self):
        if not self.players:
            return

        self.players.sort(key = operator.attrgetter("fitness"), reverse=True)
        if self.players[0].fitness > self.benchmark_fitness:
            self.staleness = 0
            self.benchmark_fitness = self.players[0].fitness
            self.champion = self.players[0].clone()
        else:
            self.staleness += 1

    def calculate_average_fitness(self):
        total_fitness = 0
        for p in self.players:
            total_fitness += p.fitness
        if self.players:
            self.average_fitness = int(total_fitness / len(self.players))
        else:
            self.average_fitness = 0

    def offspring(self):
        #------------
        if not self.players:
            baby : Player = self.champion.clone()
        elif len(self.players) > 1:
            baby : Player = self.players[random.randint(0, len(self.players) - 1)].clone()
        else:
            baby : Player = self.players[0].clone()
        #------------------
        baby.brain.mutate()
        return baby
        