from .searcher import Searcher

class GreedySearch(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(GreedySearch, self).__init__(magic_square)
        self.type = 'Greedy Search'
        self.succ_num = succ_num

    def find(self, iterations):
        super(GreedySearch, self)._init_start_state(iterations)
        
        for it in range(iterations):
            succ_idx = self.magic_square.get_succ_idx(self.succ_num)
            best_succ_idx = succ_idx[0]
            best_succ_heuristic = self.magic_square.succ_heuristic(succ_idx[0])

            # Find the best
            for curr_succ_idx in succ_idx:
                curr_succ_heuristic = (
                    self.magic_square.succ_heuristic(curr_succ_idx)
                )
                if curr_succ_heuristic < best_succ_heuristic:
                    best_succ_heuristic = curr_succ_heuristic
                    best_succ_idx = curr_succ_idx

            # Remember the best
            self.magic_square.set_succ(best_succ_idx)
            new_violation_num = self.magic_square.violation_number()
            self.all_violations.append(new_violation_num)

            if new_violation_num == 0:
                self.iter = it + 1
                break

        self.sol = self.magic_square['matrix']
        self.violation_number = self.magic_square.violation_number()
