import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
#from warehouse.warehouse_problemforGA import WarehouseProblemGA


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblemGA", num_genes: int):
        super().__init__(problem, num_genes)
        self.total_distance = None
        self.max_steps = None
        self.forklift_products = None
        self.forklift_distances = None
        # TODO self.forklifts_path = None


    def compute_fitness(self) -> float:
        self.total_distance = 0
        self.max_steps = 0

        # dividir o genoma em diferentes arrays para cada forklift
        genome_index = 0
        forklift_indexes = []
        while genome_index < len(self.genome):
            if self.genome[genome_index] > len(self.problem.products):
                forklift_indexes.append(genome_index)
            genome_index += 1
        self.forklift_products = np.split(self.genome, forklift_indexes)
        # corrigir o array -> retirar o forklift do array
        for i in range(1, len(self.problem.forklifts)):
            self.forklift_products[i] = self.forklift_products[i][1:]
        #print(forklift_products)

        # guardar distancia total, path e max_steps
        forklift = 0
        for products in self.forklift_products:
            if len(products) == 0:
                self.total_distance += self.get_pair_distance(self.problem.forklifts[forklift], self.problem.agent_search.exit)
                forklift += 1
                continue
            self.total_distance += self.get_pair_distance(self.problem.forklifts[forklift], self.problem.products[products[0] - 1])
            for i in range(1, len(products)):
                self.total_distance += self.get_pair_distance(self.problem.products[products[i - 1] - 1], self.problem.products[products[i] - 1])
            self.total_distance += self.get_pair_distance(self.problem.products[products[-1] - 1], self.problem.agent_search.exit)
            forklift += 1

        self.fitness = self.total_distance
        return self.max_steps

    def obtain_all_path(self):
        # TODO
        #return forklifts_path[][], max_steps
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
        i = 1
        for products in self.forklift_products:
            string += 'Forklift ' + str(i) + ': '
            string += str(products) + "\n\n"
            i += 1
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        new_instance.total_distance = self.total_distance
        new_instance.max_steps = self.max_steps
        new_instance.forklift_products = self.forklift_products.copy()
        return new_instance
