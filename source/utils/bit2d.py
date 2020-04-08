import numpy as np 

class BinaryIndexedTree2D():

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.a = np.zeros(shape=(n+1,m+1), dtype=int)
        self.bit = np.zeros(shape=(n+1,m+1), dtype=int)

    def set_value(self, i, j, value):
        self.inc(i, j, value - self.a[i + 1][j + 1])

    def inc(self, i, j, inc_num):
        i += 1
        j += 1
        self.a[i][j] += inc_num

        while i <= self.n:
            j1 = j
            while j1 <= self.m:
                self.bit[i][j1] += inc_num
                j1 += (j1 & -j1)
            i += (i & -i)

    def get(self, i, j):
        i += 1
        j += 1
        ret = 0

        while i >= 1:
            j1 = j
            while j1 >= 1:
                ret += self.bit[i][j1]
                j1 -= (j1 & -j1)
            i -= (i & -i)
        return ret

    def get_rect(self, i1, j1, i2, j2):
        return (+self.get(i2, j2)
                -self.get(i1 - 1, j2)
                -self.get(i2, j1 - 1)
                +self.get(i1 - 1, j1 - 1))

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        if key == 'm':
            return self.m
        if key == 'matrix':
            return self.a[1:, 1:]
        return None
