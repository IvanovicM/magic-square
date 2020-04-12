from .searcher import Searcher

class SimulatedAnnealing(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(SimulatedAnnealing, self).__init__(magic_square)
        self.type = 'Simulated Annealing'

    def find(self, iterations):
        self._init_start_state(iterations)
        
        for it in range(iterations):
            succ_idx = self.magic_square.get_succ_idx(self.succ_num)
            best_succ_idx = None
            best_succ_heuristic = self.magic_square.heuristic()

            # Find the best
            for curr_succ_idx in succ_idx:
                curr_succ_heuristic = (
                    self.magic_square.succ_heuristic(curr_succ_idx)
                )
                if curr_succ_heuristic < best_succ_heuristic:
                    best_succ_heuristic = curr_succ_heuristic
                    best_succ_idx = curr_succ_idx

            # Remember the best
            if best_succ_idx is not None:
                self.magic_square.set_succ(best_succ_idx)
            if self._should_break(it):
                break

        self.sol = self.magic_square['matrix']
        self.violation_number = self.magic_square.violation_number()