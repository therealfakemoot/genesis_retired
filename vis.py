from matplotlib import pyplot as plt
import numpy as np
from core import generate_map
from matplotlib.pyplot import contour
from functools import partial


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


def topo(noisemap, view=None, levels=None, **kwargs):
    '''Plots a topological map of a given heightmap, with an optional viewport
    for fine grained mapping.

    noisemap: DataFrame
    '''

    if not levels:
        nmax = int(max(noisemap.max()))
        nmin = int((min(noisemap.min())))
        step = (nmax - nmin) / 15
        levels = range(nmin, nmax, 500)
        con = contour(noisemap, levels, **kwargs)
    else:
        con = contour(noisemap, levels, **kwargs)
    plt.clabel(con, inline=1, fontsize=10)
    #CB = PLT.colorbar(con, extend='both')
    return con
