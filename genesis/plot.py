import logging

import matplotlib
import numpy as np
import matplotlib.pyplot as plt


logger = logging.getLogger(__name__)


def plot_map(noisemap):
    logger.info('Entering plot_map()')
    matplotlib.rcParams['xtick.direction'] = 'out'
    matplotlib.rcParams['ytick.direction'] = 'out'

    x = np.arange(0, noisemap.shape[0])
    y = np.arange(0, noisemap.shape[1])
    X, Y = np.meshgrid(x, y)

    plt.figure()
    cs = plt.contour(X, Y, noisemap._array)
    plt.clabel(cs, inline=1, fontsize=10)
    plt.title('Simplest default with labels')

    logger.info('Exiting plot_map()')
    plt.show()
