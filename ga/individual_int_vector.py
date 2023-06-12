
from abc import abstractmethod
import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.problem import Problem
from ga.individual import Individual

class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = np.full(num_genes, 0, dtype=int)
        # preencher o genoma com valores aleatórios
        added = 0
        while added < len(self.genome):
            rand = GeneticAlgorithm.rand.randint(1, len(self.genome))
            if rand not in self.genome:
                self.genome[added] = rand
                added += 1
        #print(self.genome)

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
