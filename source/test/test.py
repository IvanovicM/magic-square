from ..search import annealing, beam, genetic, greedy, randoms
from ..utils.magic import MagicSquare

if __name__ == '__main__':
    ms = MagicSquare(5)
    finders = [
        randoms.RandomSearch(ms),
        greedy.GreedySearch(ms),
        annealing.SimulatedAnnealing(ms),
        beam.LocalBeamSearch(ms),
        genetic.GeneticAlgorithm(ms)
    ]

    for finder in finders:
        finder.find(100)
        finder.print_solution()
