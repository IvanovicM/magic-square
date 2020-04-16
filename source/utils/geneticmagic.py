import numpy as np

from .magic import MagicSquare

class GeneticMagicSquare(MagicSquare):

    def reshape_square(self):
        return self.matrix.reshape((1, -1))[0]

    def square_to_chromosome(self):
        square_array = self.reshape_square()
        chromosome = np.zeros(shape=square_array.shape, dtype=int)

        for num_idx in range(len(chromosome)):
            num = square_array[num_idx]

            for i in range(num_idx):
                if square_array[i] > num:
                    chromosome[num - 1] += 1
        return chromosome

    def __getitem__(self, key):
        if key == 'chromosome':
            return self.reshape_square()
        return super(GeneticMagicSquare, self).__getitem__(key) 