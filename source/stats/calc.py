import numpy as np 

def violation_num_mean_std(finder, experiments=100, iter_per_experiment=100):
    violations = []
    for _ in range(experiments):
        finder.find(iter_per_experiment)
        violations.append(finder['viol num'])
    
    return np.mean(violations), np.std(violations)

def iteartions_mean_std(finder, experiments=100, iter_per_experiment=100):
    iteartions = []
    for _ in range(experiments):
        finder.find(iter_per_experiment)
        iteartions.append(finder['iter'])
    
    return np.mean(iteartions), np.std(iteartions)
