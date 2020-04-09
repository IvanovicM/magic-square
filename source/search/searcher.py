import numpy as np 

from ..utils.magic import MagicSquare

class Searcher():

    def __init__(self, magic_square):
        self.magic_square = magic_square
        self.sol = None

    def find(self):
        pass

    def print_solution(self):
        if self.sol is None:
            self.find()
        print('============================================================\n'
              'Search type: {}\nviolation number: {}\nsolution: \n{}'.format(
                  self.type,
                self.magic_square.violation_number(),
                self.magic_square['matrix']
        ))