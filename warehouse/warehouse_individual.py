from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from warehouse.warehouse_problemforGA import WarehouseProblemGA


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblemGA", num_genes: int):
        super().__init__(problem, num_genes)
        self.total_distance = None


    def compute_fitness(self) -> float:
        self.total_distance = 0
        for i in range(len(self.genome)):
            #TODO
            pass
        return self.total_distance

    def obtain_all_path(self):
        # TODO
        pass

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
