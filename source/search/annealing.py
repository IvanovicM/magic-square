from .searcher import Searcher

class SimulatedAnnealing(Searcher):

    def __init__(self, magic_square):
        super(SimulatedAnnealing, self).__init__(magic_square)
        self.type = 'Simulated Annealing'

    def find(self):
        pass