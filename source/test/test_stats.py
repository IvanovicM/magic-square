from ..utils.magic import MagicSquare
from ..search import annealing, beam, genetic, greedy, randoms
from ..stats import calc

def print_stats(finder):
    print('============================================================\n'
          'Search type: {}\n'.format(finder['type']))

    mean, std = calc.violation_num_mean_std(finder)
    print('-- Violation number stats --\n'
          'Max violation number: {}\n'
          'mean: {:.2f}, std: {:.2f}\n'.format(finder['max viol num'], mean, std)
    )

    mean, std = calc.iteartions_mean_std(finder, iter_per_experiment=100)
    print('-- Iterations stats --\n'
          'Iterations per experiment: {}\n'
          'mean: {:.2f}, std: {:.2f}\n'.format(100, mean, std)
    )

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
        print_stats(finder)

    