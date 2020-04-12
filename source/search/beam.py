from .searcher import Searcher

class LocalBeamSearch(Searcher):

    def __init__(self, magic_square, succ_num=30, beam_num=10):
        super(LocalBeamSearch, self).__init__(magic_square, succ_num)
        self.type = 'Local Beam Search'
        self.beam_num = beam_num

    def find(self, iterations):
        pass