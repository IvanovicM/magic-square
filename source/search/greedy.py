from .searcher import Searcher

class GreedySearch(Searcher):

    def __init__(self, magic_square):
        super(GreedySearch, self).__init__(magic_square)
        self.type = 'Greedy Search'

    def find(self, iterations):
        pass