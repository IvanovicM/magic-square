import copy

from .searcher import Searcher
from ..utils.magic import MagicSquare

class LocalBeamSearch(Searcher):

    def __init__(self, magic_square, succ_num=30, beam_num=10):
        super(LocalBeamSearch, self).__init__(magic_square, succ_num)
        self.type = 'Local Beam Search'
        self.beam_num = beam_num

    def find(self, iterations):
        self._init_start_state(iterations)

        for it in range(iterations):
            # Generate succs for every magic square
            beam_succ_idx = []
            for i in range(len(self.magic_squares)):
                succ_idx = self.magic_squares[i].get_succ_idx(self.succ_num)
                for idx in succ_idx:
                    beam_succ_idx.append((i, idx))

            # Chose beam_num best
            sorted_beam_succ_idx = sorted(beam_succ_idx, key=self._cmp_succ)
            best_beam_succ_idx = sorted_beam_succ_idx[0 : self.beam_num]        

            # Remeber beam_num best ones
            old_magic_squares = copy.deepcopy(self.magic_squares)
            self.magic_squares = []
            for x in best_beam_succ_idx:
                ms_idx = x[0]
                succ_idx = x[1]
                this_magic_square = copy.deepcopy(old_magic_squares[ms_idx])

                this_magic_square.set_succ(succ_idx)
                self.magic_squares.append(this_magic_square)
            self._set_best_magic_square()

            if self._should_break(it):
                break

    def _cmp_succ(self, x):
        magic_square_idx = x[0]
        succ_idx = x[1]
        return self.magic_squares[magic_square_idx].succ_heuristic(succ_idx)

    def _set_best_magic_square(self):
        self.magic_square = None
        for ms in self.magic_squares:
            if self.magic_square is None or (
                ms.violation_number() < self.magic_square.violation_number()
            ):
                self.magic_square = ms

    def _init_start_state(self, iterations):
        self.magic_squares = []
        self.n = self.magic_square['n']
        self.magic_square = None

        for _ in range(self.beam_num):
            ms = MagicSquare(self.n)
            ms.init_random()
            self.magic_squares.append(ms)

        self._set_best_magic_square()
        self.iter = iterations
        self.all_violations = [self['viol num']]