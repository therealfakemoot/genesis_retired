import itertools
import numpy
from pandas import DataFrame as df
import simplex
from noise import PerlinNoise
from profiler import profile_this
from random import randint
import sys
from collections import OrderedDict as od
from pdb import set_trace

#@profile_this
def generate_map(size=None, seed=None, scale=None, height=None, simp=True):
    '''Generates a table of simplex values for a two-dimensional plane.
    Parameters
    ----------
    scale : float
        'Smooths' or 'roughens' the simplex function, creating greater or 
        smaller variance in values at adjacent points. A fractional scale
        argument increases the smoothness.
    size : integer,optional
        Dictates the world's dimensions.
    seed : integer,optional
        Seed for the simplex random number generator.
    '''
    if not size:
        size = 5
    if not seed:
        seed = randint(0, sys.maxint)
    if not scale:
        scale = .0001

    print "Seed: {0}\n".format(seed)
    
    if not simp:
        #Perlin noise is currently not being used, pending further review.
        pass
        #noise = df(n)
    else:
        simplex.set_seed(seed)
        noise = _simplex(size, scale=scale)
    noise = df(noise) + 1
    return noise

def rescale(frame, height):
    '''
    frame : dataFrame
    height : integer
        Dictates the total height of geographic features of the map. Very large
        values will allow generation of maps with deep bodies of water or large
        amounts of underground volume.
    '''
    noise = frame  * height
    return noise

def _perlin(size):
    '''Returns a numpy array containing equally sized arrays.'''
    noise = PerlinNoise(size=(size,size+1))
    _,size = noise.size
    n = numpy.split(noise.getData(), size)
    return n


def _simplex(size, scale=.001):
    '''Returns a dictionary mapping keys'''
    if size %2 != 0: raise ValueError('Size parameter must be even.')
    simplices = list()
    simplex3 = simplex.simplex3
    for i in xrange(size):
        for j in xrange(size):
            simplices.append(simplex3(i*scale,j*scale,0))
    simplices = numpy.array(simplices)
    #set_trace()
    if size % 2 == 0:
        return numpy.split(simplices, size)

def coord_access(frame, coords=(0,0)):
    return frame[coords[0]][coords[1]]

if __name__ == '__main__':
    noise = generate_map(size=26, scale=.0001)
    print noise.describe()
