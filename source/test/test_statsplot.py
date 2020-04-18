from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms
from ..stats import statsplot

if __name__ == '__main__':
    ms = MagicSquare(5)
    finders = [
        randoms.RandomSearch(ms),
        greedy.GreedySearch(ms),
        annealing.SimulatedAnnealing(ms),
        beam.LocalBeamSearch(ms),
        genetic.GeneticAlgorithm(ms)
    ]
    
    # General stats plot
    for finder in finders:
        statsplot.plot_violations_through_time(finder)

    # Sim. ann. and beam stats plot
    statsplot.plot_simulated_annealing_params(finders[2])
    statsplot.plot_beam_finder_params(finders[3])
    statsplot.plot_beam_finder_params(finders[4])

    