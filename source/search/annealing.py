from math import exp
from numpy import zeros
from random import randint, uniform

from .searcher import Searcher

class SimulatedAnnealing(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(SimulatedAnnealing, self).__init__(magic_square, succ_num)
        self.type = 'Simulated Annealing'

    def find(self, iterations):
        self._init_start_state(iterations)
        self.T = [
            i / (iterations * self.magic_square['n'] / 2)
            for i in range(iterations, 0, -1)
        ]
        self.prob = zeros(shape=(iterations, 1))
        
        for it in range(iterations):
            # Chose succ randomly
            succ_idx = self.magic_square.get_succ_idx(self.succ_num)
            random_succ_idx = succ_idx[randint(0, self.succ_num - 1)]

            # Calculate sim. annealing values
            T = self.T[it]
            deltaE = (
                self.magic_square.heuristic()
                - self.magic_square.succ_heuristic(random_succ_idx)
            )

            # Go to next
            if deltaE > 0:
                self.prob[it] = 1
                self.magic_square.set_succ(random_succ_idx)
            else:
                self.prob[it] = exp(deltaE / T)
                if uniform(0, 1) < exp(deltaE / T):
                    self.magic_square.set_succ(random_succ_idx)
                    
            if self._should_break(it):
                break

    def __getitem__(self, key):
        if key == 'T':
            return self.T
        if key == 'prob':
            return self.prob
        return super(SimulatedAnnealing, self).__getitem__(key) 
