import numpy as np

from .searcher import Searcher
from ..utils.geneticmagic import GeneticMagicSquare

class GeneticAlgorithm(Searcher):

    def __init__(self, magic_square, succ_num=30, population_num=100):
        super(GeneticAlgorithm, self).__init__(magic_square, succ_num)
        self.type = 'Genetic Algorithm'
        self.population_num = population_num
        self.mean_violations = None

    def find(self, iterations):
        self._init_start_state(iterations)
        # TODO 

    def _init_start_state(self, iterations):
        self.population = []
        self.n = self.magic_square['n']
        self.magic_square = None
        self.mean_violations = []
        total_violation_sum = 0

        for _ in range(self.population_num):
            gms = GeneticMagicSquare(self.n)
            gms.init_random()
            self.population.append(gms)

            total_violation_sum += gms.violation_number()

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

    def _chromosome_to_square(self, chromosome):
        pos = np.zeros(shape=chromosome.shape, dtype=int)
        for i in range(len(chromosome)-1, -1, -1):
            pos[i] = chromosome[i]
            for j in range(i + 1, len(chromosome)):
                if pos[j] >= pos[i]:
                    pos[j] += 1

        square = np.zeros(shape=chromosome.shape, dtype=int)
        for i in range(len(chromosome)):
            square[pos[i]] = i + 1
        return square.reshape((self.magic_square['n'], -1))

    def __getitem__(self, key):
        if key == 'mean viol. through iter.':
            return self.mean_violations
        return super(GeneticAlgorithm, self).__getitem__(key) 