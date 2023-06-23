from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        num_genes = len(ind.genome)
        for i in range(num_genes):
            ind.genome[i] = num_genes + 1 - ind.genome[i]

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
