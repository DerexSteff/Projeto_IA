import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        parent1 = ind1.genome
        parent2 = ind2.genome

        ind1.genome = self.ox(parent1, parent2)
        ind2.genome = self.ox(parent2, parent1)

    def ox(self, parent1, parent2):
        length = len(parent1)
        # choose random indexes
        index1 = GeneticAlgorithm.rand.randint(1, length - 1)
        index2 = GeneticAlgorithm.rand.randint(index1 + 1, length)

        child = [-1] * length
        child[index1:index2+1] = parent1[index1:index2+1]

        for i in range(length):
            if child[i] == -1:
                for value in parent2:
                    if value not in child:
                        child[i] = value
                        break
        return child

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"