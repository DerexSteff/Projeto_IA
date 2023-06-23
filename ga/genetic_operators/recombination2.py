from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        cut1 = [-1] * num_genes
        cut2 = [-1] * num_genes
        start_pos = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        end_pos = GeneticAlgorithm.rand.randint(start_pos + 1, num_genes)

        cut1[start_pos:end_pos] = ind1.genome[start_pos:end_pos]
        cut2[start_pos:end_pos] = ind2.genome[start_pos:end_pos]

        j1 = 0
        j2 = 0
        for i in range(num_genes):
            if ind2.genome[i] not in cut1:
                if cut1[j1] == -1:
                    cut1[j1] = ind2.genome[i]
                    j1 += 1
            if ind1.genome[i] not in cut2:
                if cut2[j2] == -1:
                    cut2[j2] = ind1.genome[i]
                    j2 += 1

        ind1.genome = cut1
        ind2.genome = cut2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
