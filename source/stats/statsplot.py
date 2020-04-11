import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def plot_violations_through_time(finder, iter_per_experiment=100):
    finder.find(iter_per_experiment)
    all_violations = finder['viol. through iter.']

    plt.plot(all_violations)
    plt.title(finder['type'])
    plt.xlabel('iterations')
    plt.ylabel('violations num')
    plt.show()
    

