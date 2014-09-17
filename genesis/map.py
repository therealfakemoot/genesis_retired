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
    def __init__(self, size, seed=None, scale=.001):
        pass
