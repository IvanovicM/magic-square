from .searcher import Searcher

class RandomSearch(Searcher):

    def __init__(self, magic_square):
        super(RandomSearch, self).__init__(magic_square)
        self.type = 'Random Search'

    def find(self, iterations):
        super(RandomSearch, self)._init_start_state(iterations)

        for _ in range(iterations - 1):
            self.magic_square.init_random()
            new_violation_number = self.magic_square.violation_number()

            if new_violation_number < self.violation_number:
                self.sol = self.magic_square['matrix']
                self.violation_number = new_violation_number
                self.all_violations.append(new_violation_number)
            
            if new_violation_number == 0:
                self.iter = it + 1
                break
        