import numpy as np 

from ..utils.magic import MagicSquare

class Searcher():

    def __init__(self, magic_square, succ_num):
        self.magic_square = magic_square
        self.max_violation_number = (self.magic_square['n'] + 1) * 2
        self.iter = None
        self.all_violations = None
        self.succ_num = succ_num

    def find(self, iterations):
        pass

    def print_solution(self):
        if self.magic_square is None:
            return
        print('============================================================\n'
              'Search type: {}\n'
              'iterations: {}\n'
              'violation number: {} of {}\n'
              'solution: \n{}'.format(
                    self.type, self.iter, self['viol num'],
                    self.max_violation_number, self['sol']
        ))

    def _init_start_state(self, iterations):
        self.magic_square.init_random()
        self.iter = iterations
        self.all_violations = [self['viol num']]

    def _should_break(self, curr_it):
        new_violation_num = self.magic_square.violation_number()
        self.all_violations.append(new_violation_num)
        if new_violation_num == 0:
            self.iter = curr_it + 1
            return True
        return False

    def __getitem__(self, key):
        if key == 'sol':
            return self.magic_square['matrix']
        if key == 'viol num':
            return self.magic_square.violation_number()
        if key == 'max viol num':
            return self.max_violation_number
        if key == 'type':
            return self.type
        if key == 'iter':
            return self.iter
        if key == 'viol. through iter.':
            return self.all_violations
        return None