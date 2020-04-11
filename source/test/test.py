from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms

if __name__ == '__main__':
    ms = MagicSquare(5)

    #finder = randoms.RandomSearch(ms)
    finder = greedy.GreedySearch(ms)

    finder.find(10000)
    finder.print_solution()
