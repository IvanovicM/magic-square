import numpy as np
import random

from .bit2d import BinaryIndexedTree2D

class MagicSquare():

    def __init__(self, n):
        self.n = n
        self.sum_map = {}
        self.matrix = np.zeros(shape=(n, n), dtype=int)
        self.sum = int(n * (n**2 + 1) / 2)
        self.all_indeces = [[i,j] for i in range(n) for j in range(n)]
        self.init_random()

    def init_random(self):
        self.init_sum_map()

        rm = np.random.permutation(self.n * self.n).reshape((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                self.set_value(i, j, rm[i][j] + 1)

    def init_sum_map(self):
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
        return self.violation_number()

    def succ_heuristic(self):
        pass

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
        return None