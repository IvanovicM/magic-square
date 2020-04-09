from .searcher import Searcher

class GeneticAlgorithm(Searcher):

    def __init__(self, magic_square):
        super(GeneticAlgorithm, self).__init__(magic_square)
        self.type = 'Genetic Algorithm'

    def find(self):
        pass