import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import guppy

from genesis.map import Map


def plot_map(noisemap):
    matplotlib.rcParams['xtick.direction'] = 'out'
    matplotlib.rcParams['ytick.direction'] = 'out'

    x = np.arange(0, noisemap.shape[0])
    y = np.arange(0, noisemap.shape[1])
    X, Y = np.meshgrid(x, y)
    #difference of Gaussians

    # Create a simple contour plot with labels using default colors.  The
    # inline argument to clabel will control whether the labels are draw
    # over the line segments of the contour, removing the lines beneath
    # the label
    plt.figure()
    cs = plt.contour(X, Y, noisemap._array)
    plt.clabel(cs, inline=1, fontsize=10)
    plt.title('Simplest default with labels')

    plt.show()


def memtest():
    x, y = 100, 100
    for i in range(1, 20):
        hp = guppy.hpy()
        X, Y = x * i, y * 1
        hp.setref()
        m = Map((x, y))
        plot_map(m)
        h = hp.heap()
        h.dump('{x}by{y}.prof'.format(x=X, y=Y))
