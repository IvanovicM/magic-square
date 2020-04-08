import numpy as np

from bit2d import BinaryIndexedTree2D

class MagicSquare():

    def __init__(self, n):
        self.bit = BinaryIndexedTree2D(n, n)
        self.sum = int(n * (n**2 + 1) / 2)

    def init_random(self):
        # TODO
        return None

    def violation_number(self):
        if (self.bit is None):
            return None
        # TODO
        return 0

    def get_successors(self, succ_num):
        # TODO
        return None

    def __getitem__(self, key):
        if key == 'n':
            return self.bit['n']
        if key == 'sum':
            return self.sum
        if key == 'matrix':
            return self.bit['matrix']
        return None