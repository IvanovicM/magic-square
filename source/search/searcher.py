import numpy as np 

from ..utils.magic import MagicSquare

class Searcher():

    def __init__(self, magic_square):
        self.magic_square = magic_square
        self.sol = None
        self.violation_number = None
        self.iter = None

    def find(self, iterations):
        pass

    def print_solution(self):
        if self.sol is None:
            return
        print('============================================================\n'
              'Search type: {}\n'
              'iterations: {}\n'
              'violation number: {}\n'
              'solution: \n{}'.format(
                    self.type, self.iter, self.violation_number, self.sol
        ))

    def __getitem__(self, key):
        if key == 'sol':
            return self.sol
        if key == 'viol_num':
            return self.violation_number
        if key == 'type':
            return self.type
        if key == 'iter':
            return self.iter
        return None