from .searcher import Searcher

class LocalBeamSearch(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(LocalBeamSearch, self).__init__(magic_square, succ_num)
        self.type = 'Local Beam Search'

    def find(self, iterations):
        pass