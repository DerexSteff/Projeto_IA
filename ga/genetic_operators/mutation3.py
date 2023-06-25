from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        """
        Mutation: pick 2 random values from genome and swap them
        """

        # pick random indexes
        index1 = 0
        index2 = 0
        length = len(ind.genome)
        while index1 == index2:
            index1 = GeneticAlgorithm.rand.randint(1, length - 1)
            index2 = GeneticAlgorithm.rand.randint(1, length - 1)

        # adjust indexes
        if index1 > index2:
            index1, index2 = index2, index1

        # swap values
        ind.genome[index1], ind.genome[index2] = ind.genome[index2], ind.genome[index1]

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
