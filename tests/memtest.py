import guppy

from genesis.map import Map
from genesis.plot import plot_map


def guppy_memtest():
    x, y = 100, 100
    for i in range(1, 20):
        hp = guppy.hpy()
        X, Y = x * i, y * 1
        hp.setref()
        m = Map((x, y))
        plot_map(m)
        h = hp.heap()
        h.dump('{x}by{y}.prof'.format(x=X, y=Y))


def memtest(profiler):
    if profiler == 'guppy':
        guppy_memtest()
