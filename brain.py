from NN import dense, sigmoid
import numpy as np
import copy
import random

class Brain:
    def __init__(self, inputs):
        self.inputs = inputs
        self.vision = None

    def generate_network(self):
        self.network = [
            dense.Dense(self.inputs,2),
            sigmoid.Sigmoid(),
            dense.Dense(2,1),
            sigmoid.Sigmoid()
        ]

    def feed_foward(self, vision):
        self.vision = np.append(vision, 1)
        self.vision = np.reshape(self.vision, shape=(self.vision.shape[0],1))
        output = self.vision
        
        for layer in self.network:
            output = layer.foward(output)
        return output

    def clone(self):
        clone = Brain(self.inputs)

        clone.network = copy.deepcopy(self.network)
        
        return clone

    def mutate(self):
        if random.uniform(0,1) < 0.8:
            for l in self.network:
                if isinstance(l, dense.Dense):

                    # Decide individualmente o tipo de mutação de cada peso
                    strong_mutation = np.random.random(l.weights.shape) < 0.1

                    # Mutação forte: substitui o peso
                    strong_values = np.random.uniform(
                        -1, 1, size=l.weights.shape
                    )

                    # Mutação leve: adiciona ruído ao peso
                    weak_values = np.random.normal(
                        0, 0.1, size=l.weights.shape
                    )

                    l.weights = np.where(
                        strong_mutation,
                        strong_values,
                        l.weights + weak_values
                    )
        
