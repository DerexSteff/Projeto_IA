from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination
import numpy as np

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        cycle = []
        index = 0
        while True:
            cycle.append(index)
            value = ind1.genome[index]
            index = np.where(ind2.genome == value)[0][0]
            if index == cycle[0]:
                break

        offspring1 = np.where(np.isin(ind1.genome, ind1.genome[cycle]), ind1.genome, ind2.genome)
        offspring2 = np.where(np.isin(ind2.genome, ind2.genome[cycle]), ind2.genome, ind1.genome)

        ind1.genome = offspring1
        ind2.genome = offspring2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
