from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms
from ..stats import calc

def print_stats(finder, iter_per_experiment=100):
    print('============================================================\n'
          'Search type: {}\n'.format(finder['type']))

    it_mean, it_std, viol_mean, viol_std = calc.stats_mean_std(
        finder, iter_per_experiment=iter_per_experiment
    )
    print('-- Violation number stats --\n'
          'Max violation number: {}\n'
          'mean: {:.2f}, std: {:.2f}\n'.format(
                finder['max viol num'], viol_mean, viol_std
        )
    )

    print('-- Iterations stats --\n'
          'Iterations per experiment: {}\n'
          'mean: {:.2f}, std: {:.2f}\n'.format(
                iter_per_experiment, it_mean, it_std
        )
    )

if __name__ == '__main__':
    ms = MagicSquare(3)
    finders = [
        randoms.RandomSearch(ms),
        greedy.GreedySearch(ms),
        annealing.SimulatedAnnealing(ms),
        beam.LocalBeamSearch(ms),
        genetic.GeneticAlgorithm(ms)
    ]
    
    for finder in finders:
        print_stats(finder)

    