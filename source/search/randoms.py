from .searcher import Searcher

class RandomSearch(Searcher):

    def __init__(self, magic_square):
        super(RandomSearch, self).__init__(magic_square)
        self.type = 'Random Search'

    def find(self):
        pass