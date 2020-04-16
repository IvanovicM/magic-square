import numpy as np

from .searcher import Searcher
from ..utils.magic import MagicSquare

class GeneticAlgorithm(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(GeneticAlgorithm, self).__init__(magic_square, succ_num)
        self.type = 'Genetic Algorithm'

    def find(self, iterations):
        pass 

    def chromosome_to_square(self, chromosome):
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