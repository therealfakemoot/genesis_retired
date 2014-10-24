from itertools import izip_longest, product
from functools import partial

import numpy as np
import noise


def view(frame, viewport):
    '''
    Returns a windowed version of the dataframe.
    viewport: tuple
        A tuple of the form (x,y,height,width)
    '''

    x, y, h, w = viewport
    return frame.ix[x:x + w, y:y + h]


def chunk(frame, viewport):
    '''
    Slices a DataFrame into smaller, equal-sized DataFrames according to viewport.
    viewport: tuple
        A tuple of the form (x,y,height,width)
    '''

    xmax, ymax = frame.shape
    x, y, h, w = viewport
    if any(n % 2 != 0 for n in viewport):
        raise ValueError('Viewport values must be even integers.')
    if h != w:
        raise ValueError('Viewport must be of equal dimensions.')
    chunks = xmax / w
    fview = partial(view, frame)
    for i in range(chunks):
        for j in range(chunks):
            yield fview((y + h * j, x + w * i, h - 1, w - 1))


def ichunk(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def map_noise(height, width, z, scale=.001):
    '''Creates a sequence of values representing simplex noise.
    Parameters
    ----------

    height : integer
        Assuming the origin is in the lower left corner, height controls
        the maximum value of the y axis of the map.
    width : integer
        Controls the maximum value of the x axis, as per the `height`
        parameter.
    z : integer
        The z parameter scales the 'height' or z-axis of the map when considered
        in three dimensions, with height and width providing x and y.
    '''
    coords = product(range(height), range(width))
    for x, y in coords:
        yield noise.snoise3(x * scale, y * scale, 0) * z


class Map(object):
    def __init__(self, shape, height=1000000, seed=None, scale=.0001):
        self.shape = shape
        self._array = np.asarray(list(ichunk(map_noise(*shape, z=height, scale=scale), shape[1])))

    def __getitem__(self, key):
        return self._array[key[0]][key[1]]
