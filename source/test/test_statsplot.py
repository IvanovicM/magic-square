from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms
from ..stats import statsplot

if __name__ == '__main__':
    ms = MagicSquare(5)

    #finder = randoms.RandomSearch(ms)
    #finder = greedy.GreedySearch(ms)
    #finder = annealing.SimulatedAnnealing(ms)
    #finder = beam.LocalBeamSearch(ms)
    finder = genetic.GeneticAlgorithm(ms)
    
    #statsplot.plot_violations_through_time(finder)
    #statsplot.plot_simulated_annealing_params(finder)
    statsplot.plot_beam_finder_params(finder)

    