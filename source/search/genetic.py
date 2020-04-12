from .searcher import Searcher

class GeneticAlgorithm(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(GeneticAlgorithm, self).__init__(magic_square, succ_num)
        self.type = 'Genetic Algorithm'

    def find(self, iterations):
        pass