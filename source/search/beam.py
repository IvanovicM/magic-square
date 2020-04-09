from .searcher import Searcher

class LocalBeamSearch(Searcher):

    def __init__(self, magic_square):
        super(LocalBeamSearch, self).__init__(magic_square)
        self.type = 'Local Beam Search'

    def find(self):
        pass