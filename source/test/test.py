from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms

if __name__ == '__main__':
    ms = MagicSquare(3)

    #fnd = randoms.RandomSearch(ms)
    fnd = greedy.GreedySearch(ms)

    fnd.find(100)
    fnd.print_solution()
