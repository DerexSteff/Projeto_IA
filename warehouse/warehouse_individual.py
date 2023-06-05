from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
#from warehouse.warehouse_problemforGA import WarehouseProblemGA


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblemGA", num_genes: int):
        super().__init__(problem, num_genes)
        self.total_distance = None
        self.max_steps = None
        # TODO self.forklifts_path = None


    def compute_fitness(self) -> float:
        self.total_distance = 0
        self.max_steps = 0

        # .pptx crossover algorithms crossover operators for permutation ; slide 31
        #print("INDIVIDUAL**************************************")
        #print("GENOME: ", self.genome)
        genome_index = 0
        for forklift in self.problem.forklifts:
            if genome_index >= len(self.genome) or self.genome[genome_index] > len(self.problem.products):
                self.total_distance += self.get_pair_distance(forklift, self.problem.agent_search.exit)
                genome_index += 1
                continue

            # forklift -> 1º do genoma
            self.total_distance += self.get_pair_distance(forklift, self.problem.products[self.genome[genome_index] - 1])
            genome_index += 1

            # enquanto nao encontra outro forklift ou nao acabou genoma
            while genome_index < len(self.genome) and self.genome[genome_index] <= len(self.problem.products):
                self.total_distance += self.get_pair_distance(self.problem.products[self.genome[genome_index-1] - 1], self.problem.products[self.genome[genome_index] - 1])
                genome_index += 1
            # forklift -> exit
            self.total_distance += self.get_pair_distance(self.problem.products[self.genome[genome_index-1] - 1], self.problem.agent_search.exit)
            genome_index += 1
            #print("forklift: ", forklift, "total_distance: ", self.total_distance)

        self.fitness = self.total_distance
        return self.max_steps

    def obtain_all_path(self):
        # TODO
        #return forklifts_path, max_steps
        # incluir posicao inicial forklift
        pass

    def get_pair_distance(self, cell1, cell2):
        for p in self.problem.agent_search.pairs:
            if (p.cell1 == cell1 and p.cell2 == cell2) or (p.cell1 == cell2 and p.cell2 == cell1):
                return p.value
        return None

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance
