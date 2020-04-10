from .searcher import Searcher

class GreedySearch(Searcher):

    def __init__(self, magic_square, succ_num=30):
        super(GreedySearch, self).__init__(magic_square)
        self.type = 'Greedy Search'
        self.succ_num = succ_num

    def find(self, iterations):
        super(GreedySearch, self)._init_start_state(iterations)
        
        for it in range(iterations):
            succs = self.magic_square.get_successors(self.succ_num)
            best_succ = succs[0]
            best_succ_heuristic = best_succ.heuristic()

            for curr_succ in succs:
                curr_succ_heuristic = curr_succ.heuristic()
                if curr_succ_heuristic < best_succ_heuristic:
                    best_succ_heuristic = curr_succ_heuristic
                    best_succ = curr_succ

            self.magic_square = best_succ
            new_violation_num = best_succ.violation_number()
            self.all_violations.append(new_violation_num)

            if new_violation_num == 0:
                self.iter = it + 1
                break

        self.sol = self.magic_square['matrix']
        self.violation_number = self.magic_square.violation_number()
