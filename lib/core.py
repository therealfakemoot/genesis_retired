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
def generate_map(size=None, seed=None, scale=None, height=None, simp=False):
    '''Generates a table of simplex values for a two-dimensional plane.
    Parameters
    ----------
    size : integer,optional
        Dictates the world's dimensions.
    seed : integer,optional
        Seed for the simplex random number generator.
    scale : float,optional
        'Smooths' or 'roughens' the simplex function, creating greater or 
        smaller variance in values at adjacent points. A fractional scale
        argument increases the smoothness.
    height : integer,optional
        Dictates the total height of geographic features of the map. Very large
        values will allow generation of maps with deep bodies of water or large
        amounts of underground volume.
    '''
    if height is None:
        height = 15000
    if not scale:
        scale = .00001
    if not size:
        size = 5
    if not seed:
        seed = randint(0, sys.maxint)
    simplex.set_seed(seed)

    print "Seed: {0}\n".format(seed)

    
    if not simp:
        noise = df(n)
    else:
        noise = _simplex(size)
        #set_trace()
    noise = df(noise)
    noise = noise * scale
    noise = (noise + 1) * height
    return noise

def _perlin(size):
    '''Returns a numpy array containing equally sized arrays.'''
    noise = PerlinNoise(size=(size,size+1))
    _,size = noise.size
    n = numpy.split(noise.getData(), size)
    return n


def _simplex(size):
    '''Returns a dictionary mapping keys'''
    simplices = list()
    simplex3 = simplex.simplex3
    for x,y in itertools.combinations(range(size+1),2):
        simplices.append(simplex3(x,y,0))
    simplices = numpy.array(simplices)
    #set_trace()
    return numpy.split(simplices, size+1)

def coord_access(frame, coords=(0,0)):
    return frame[coords[0]][coords[1]]

if __name__ == '__main__':
    noise = generate_map(size=4, scale=.00001, simp=True)
    print noise.describe()
