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

    ind = list()
    simplices = od() 
    
    if not simp:
        noise = PerlinNoise(size=(size,size+1))
        _,size = noise.size
        n = numpy.split(noise.getData(), size)
        return df(n)
    
    simplex3 = simplex.simplex3
    for i in range(-size, size+1):
        simplices[i] = list()
        ind.append(i)
        for j in range(-size, size+1):
            simp = simplex3(i*scale,j*scale,0)
            simplices[i].append(simp)

    #set_trace()

    noise = df(simplices, index=ind)
    noise = (noise + 1) * height
    return noise

def coord_access(frame, coords=(0,0)):
    return frame[coords[0]][coords[1]]

if __name__ == '__main__':
    noise = generate_map(size=500, scale=.00001, simp=True)
