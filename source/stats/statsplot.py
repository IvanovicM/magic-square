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

def plot_simulated_annealing_params(finder, iter_per_experiment=100):
    finder.find(iter_per_experiment)
    plt.suptitle(finder['type'])

    ax1 = plt.subplot(311)
    plt.plot(finder['T'], label='T', color='green')
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.legend()

    ax2 = plt.subplot(312, sharex=ax1)
    plt.plot(finder['prob'], label='probability', color='blue')
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.legend()

    ax3 = plt.subplot(313, sharex=ax1)
    plt.plot(finder['viol. through iter.'], label='violations', color='red')
    plt.legend()

    plt.show()

def plot_beam_finder_params(finder, iter_per_experiment=100):
    finder.find(iter_per_experiment)
    all_violations = finder['viol. through iter.']
    mean_violations = finder['mean viol. through iter.']

    plt.plot(all_violations, label='min violation')
    plt.plot(mean_violations, label='violations mean')
    plt.title(finder['type'])
    plt.xlabel('iterations')
    plt.ylabel('violations num')
    plt.legend()
    plt.show()
