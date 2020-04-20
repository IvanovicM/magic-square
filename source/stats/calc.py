import numpy as np 

def violation_num_mean_std(finder, experiments=100, iter_per_experiment=100):
    violations = []
    for _ in range(experiments):
        finder.find(iter_per_experiment)
        violations.append(finder['viol num'])
    
    return np.mean(violations), np.std(violations)

def iterations_mean_std(finder, experiments=100, iter_per_experiment=100):
    iterations = []
    for _ in range(experiments):
        finder.find(iter_per_experiment)
        iterations.append(finder['iter'])
    
    return np.mean(iterations), np.std(iterations)

def stats_mean_std(finder, experiments=100, iter_per_experiment=100):
    iterations = []
    violations = []
    for _ in range(experiments):
        finder.find(iter_per_experiment)
        iterations.append(finder['iter'])
        violations.append(finder['viol num'])
    
    return (np.mean(iterations), np.std(iterations),
            np.mean(violations), np.std(violations))
