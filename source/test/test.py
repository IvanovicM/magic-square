from ..search import annealing, beam, genetic, greedy, randoms
from ..utils.magic import MagicSquare

if __name__ == '__main__':
    ms = MagicSquare(3)

    #finder = randoms.RandomSearch(ms)
    #finder = greedy.GreedySearch(ms)
    finder = annealing.SimulatedAnnealing(ms)

    finder.find(100)
    finder.print_solution()
