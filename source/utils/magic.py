import numpy as np
import random

from .bit2d import BinaryIndexedTree2D

class MagicSquare():

    def __init__(self, n):
        self.n = n
        self.bit = BinaryIndexedTree2D(n, n)
        self.sum = int(n * (n**2 + 1) / 2)
        self.all_indeces = [[i,j] for i in range(n) for j in range(n)]

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

    def heuristic(self):
        return self.violation_number()

    def get_successors(self, succ_num):
        successors = []
        for _ in range(succ_num):
            ridx = random.sample(self.all_indeces, 2)
            ridx_0 = ridx[0]
            ridx_1 = ridx[1]

            succ_mat = self.bit['matrix'].copy()
            succ_mat[ridx_0[0]][ridx_0[1]], succ_mat[ridx_1[0]][ridx_1[1]] = (
                succ_mat[ridx_1[0]][ridx_1[1]], succ_mat[ridx_0[0]][ridx_0[1]]
            )

            new_ms = MagicSquare(self.n)
            new_ms.set_matrix(succ_mat)
            successors.append(new_ms)

        return successors

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        if key == 'sum':
            return self.sum
        if key == 'matrix':
            return self.bit['matrix']
        return None