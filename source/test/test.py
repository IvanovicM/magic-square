from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms

if __name__ == '__main__':
    ms = MagicSquare(5)

    rnd = randoms.RandomSearch(ms)
    rnd.find(10)
    rnd.print_solution()
