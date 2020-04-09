import numpy as np

from .bit2d import BinaryIndexedTree2D

class MagicSquare():

    def __init__(self, n):
        self.n = n
        self.bit = BinaryIndexedTree2D(n, n)
        self.sum = int(n * (n**2 + 1) / 2)
        self.init_random()

    def init_random(self):
        rm = np.random.permutation(self.n * self.n).reshape((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                self.bit.set_value(i, j, rm[i][j] + 1)

    def set_value(self, i, j, value):
        self.bit.set_value(i, j, value)

    def set_matrix(self, matrix):
        for i in range(self.n):
            for j in range(self.n):
                self.bit.set_value(i, j, matrix[i][j])

    def violation_number(self):
        if self.bit is None:
            return None

        total_num = 0
        diag_1_sum = 0
        diag_2_sum = 0
        for i in range(self.n):
            sum = self.bit.get_rect(i, 0, i, self.n - 1)
            if sum != self.sum:
                total_num += 1

            sum = self.bit.get_rect(0, i, self.n - 1, i)
            if sum != self.sum:
                total_num += 1
            
            diag_1_sum += self.bit['matrix'][i, i]
            diag_2_sum += self.bit['matrix'][i, self.n - i - 1]

        if diag_1_sum != self.sum:
            total_num += 1
        if diag_2_sum != self.sum:
            total_num += 1
        return total_num

    def get_successors(self, succ_num):
        # TODO
        return None

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        if key == 'sum':
            return self.sum
        if key == 'matrix':
            return self.bit['matrix']
        return None