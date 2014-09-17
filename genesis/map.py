from itertools import izip_longest, product

import numpy as np
import noise


def chunk(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def map_noise(height, width, z, scale=.001):
    coords = product(range(height), range(width))
    for x, y in coords:
        yield noise.snoise3(x * scale, y * scale, 0) * z


class Map(object):
    def __init__(self, shape, height=1000000, seed=None, scale=.0001):
        self.shape = shape
        self._array = np.asarray(list(chunk(map_noise(*shape, z=height, scale=scale), shape[1])))

    def __getitem__(self, key):
        return self._array[key[0]][key[1]]
