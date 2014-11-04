import random

import numpy as np

from genesis.map import ichunk

class IntMap(object):
    def __init__(self, shape, height=1000000, seed=None, scale=.0001):
        self._array = np.asarray(list(ichunk([random.randint(0, height) for i in range(shape[0] * shape[1])], shape[1])))
        self.shape = self._array.shape

    def __getitem__(self, key):
        return self._array[key[0]][key[1]]
