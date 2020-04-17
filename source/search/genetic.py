import copy
import numpy as np
import random

from .searcher import Searcher
from ..utils.magic import MagicSquare

class GeneticAlgorithm(Searcher):

    def __init__(self, magic_square, succ_num=30, population_num=4):
        super(GeneticAlgorithm, self).__init__(magic_square, succ_num)
        self.type = 'Genetic Algorithm'
        self.population_num = population_num
        self.elite_size = 1
        self.mutation_rate = 0.1
        self.mean_violations = None

    def find(self, iterations):
        self._init_start_state(iterations)
        # TODO

    def _crossover_population(self, mating_pool):
        mating_pool = self._get_mating_pool()
        children = []
        for i in range(self.elite_size):
            children.append(mating_pool[i])
        
        # TODO: breed by probability
        mating_pool = random.sample(mating_pool, len(mating_pool))
        for i in range(len(mating_pool) - self.elite_size):
            child = self._crossover(
                mating_pool[i],
                mating_pool[len(mating_pool) - i - 1]
            )
            children.append(child)
        return children

    def _get_mating_pool(self):
        # TODO: by probability
        mating_pool = self.population
        mating_pool = random.sample(mating_pool, len(mating_pool))
        return sorted(mating_pool, key=self._fitness)

    def _crossover(self, parent_a, parent_b):
        parent_a = parent_a['matrix'].reshape((1, -1))[0]
        parent_b = parent_b['matrix'].reshape((1, -1))[0]
        parent_a_part = []
        parent_b_part = []

        gene_a = int(random.random() * len(parent_a))
        gene_b = int(random.random() * len(parent_a))
        start_gene = min(gene_a, gene_b)
        end_gene = max(gene_a, gene_b)

        for i in range(start_gene, end_gene):
            parent_a_part.append(parent_a[i])
        parent_b_part = [x for x in parent_b if x not in parent_a_part]

        child = parent_a_part + parent_b_part
        child = np.reshape(child, (self.magic_square['n'], -1))
        child_ms = MagicSquare(self.magic_square['n'])
        child_ms.set_matrix(child)
        return child_ms

    def _mutate_population(self):
        nonmutated_population = copy.deepcopy(self.population)
        self.population = []
        
        for individual in nonmutated_population:
            mutated_individual = self._mutate(individual)
            self.population.append(mutated_individual)

    def _mutate(self, individual):
        mutated_individual = copy.deepcopy(individual)
        if random.random() < self.mutation_rate:
            idx_to_swap = individual.get_succ_idx(1)
            mutated_individual.set_succ(idx_to_swap[0])
        return mutated_individual

    def _fitness(self, x):
        return x.violation_number()

    def _init_start_state(self, iterations):
        self.population = []
        self.n = self.magic_square['n']
        self.magic_square = None
        self.mean_violations = []
        total_violation_sum = 0

        for _ in range(self.population_num):
            ms = MagicSquare(self.n)
            ms.init_random()
            self.population.append(ms)

            total_violation_sum += ms.violation_number()

        self._set_best_magic_square()
        self.iter = iterations
        self.all_violations = [self['viol num']]

    def _set_best_magic_square(self):
        self.magic_square = None
        total_violation_sum = 0

        for ms in self.population:
            if self.magic_square is None or (
                ms.violation_number() < self.magic_square.violation_number()
            ):
                self.magic_square = ms
            total_violation_sum += ms.violation_number()
        
        self.mean_violations.append(total_violation_sum / self.population_num)

    def __getitem__(self, key):
        if key == 'mean viol. through iter.':
            return self.mean_violations
        return super(GeneticAlgorithm, self).__getitem__(key) 