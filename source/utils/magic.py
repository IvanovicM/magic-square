import numpy as np
import random

from .heuristics import h1, h2

class MagicSquare():

    def __init__(self, n):
        self.n = n
        self.sum_map = {}
        self.sum = int(n * (n**2 + 1) / 2)
        self.all_indeces = [[i,j] for i in range(n) for j in range(n)]
        self.init_random()

    def init_random(self):
        self._reset()
        rm = np.random.permutation(self.n * self.n).reshape((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                self.set_value(i, j, rm[i][j] + 1)

    def _reset(self):
        self.matrix = np.zeros(shape=(self.n, self.n), dtype=int)
        for i in range(self.n):
            self.sum_map['r{}'.format(i)] = 0
            self.sum_map['c{}'.format(i)] = 0

        self.sum_map['d0'] = 0
        self.sum_map['d1'] = 0
        
    def set_value(self, i, j, value):
        inc_value = value - self.matrix[i][j]
        self.matrix[i][j] = value

        self.sum_map['r{}'.format(i)] += inc_value
        self.sum_map['c{}'.format(j)] += inc_value
        if i == j:
            self.sum_map['d0'] += inc_value
        if i + j + 1 == self.n:
            self.sum_map['d1'] += inc_value

    def set_matrix(self, matrix):
        for i in range(self.n):
            for j in range(self.n):
                self.set_value(i, j, matrix[i][j])

    def violation_number(self):
        total_num = 0
        for i in range(self.n):
            total_num += int(self.sum != self.sum_map['r{}'.format(i)])
            total_num += int(self.sum != self.sum_map['c{}'.format(i)])

        total_num += int(self.sum != self.sum_map['d0'])
        total_num += int(self.sum != self.sum_map['d1'])

        return total_num

    def heuristic(self):
        return h2(self)

    def succ_heuristic(self, succ_idx):
        self._swap_values(succ_idx)
        succ_heuristic = self.heuristic()
        self._swap_values(succ_idx)
        return succ_heuristic

    def _swap_values(self, idxs):
        [i0, j0] = idxs[0]
        [i1, j1] = idxs[1]
        prev_value_0 = self.matrix[i0, j0]
        prev_value_1 = self.matrix[i1, j1]

        self.set_value(i0, j0, prev_value_1)
        self.set_value(i1, j1, prev_value_0)

    def set_succ(self, succ_idx):
        if succ_idx is None:
            return
        self._swap_values(succ_idx)

    def get_succ_idx(self, succ_num):
        succ_idx = []
        for _ in range(succ_num):
            ridx = random.sample(self.all_indeces, 2)
            succ_idx.append(ridx)

        return succ_idx

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        if key == 'sum':
            return self.sum
        if key == 'matrix':
            return self.matrix
        if key == 'sum_map':
            return self.sum_map
        return None