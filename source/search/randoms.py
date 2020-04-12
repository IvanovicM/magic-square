from random import randint
from .searcher import Searcher

class RandomSearch(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(RandomSearch, self).__init__(magic_square, succ_num)
        self.type = 'Random Search'

    def find(self, iterations):
        self._init_start_state(iterations)

        for it in range(iterations):
            succ_idx = self.magic_square.get_succ_idx(self.succ_num)
            random_succ_idx = randint(0, self.succ_num - 1)
            next_succ_idx = succ_idx[random_succ_idx]

            # Remember that randomly chosen
            self.magic_square.set_succ(next_succ_idx)
            if self._should_break(it):
                break
        