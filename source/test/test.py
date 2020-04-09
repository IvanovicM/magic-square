from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms

if __name__ == '__main__':
    ms = MagicSquare(5)

    an = annealing.SimulatedAnnealing(ms)
    an.print_solution()

    loc_beam = beam.LocalBeamSearch(ms)
    loc_beam.print_solution()

    gen = genetic.GeneticAlgorithm(ms)
    gen.print_solution()

    gr = greedy.GreedySearch(ms)
    gr.print_solution()

    rnd = randoms.RandomSearch(ms)
    rnd.print_solution()
