from pandas import DataFrame as df
from lib import simplex
from lib.profiler import profile_this
from random import randint
import sys
from collections import OrderedDict as od
from pdb import set_trace

#@profile_this
def generate_map(size=None, seed=None, scale=None, height=None):
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
    if not height:
        height = 15000
    else:
        height = height
    if not scale:
        scale = .000000000000000001
    if not size:
        size = 5
    if not seed:
        seed = randint(0, sys.maxint)
    simplex.set_seed(seed)

    print "Seed: {0}\n".format(seed)

    ind = list()
    simplices = od() 

    for i in range(-size, size+1):
        key = 'X({})'.format(i)
        simplices[key] = list()
        ind.append('Y({})'.format(i))
        for j in range(-size, size+1):
            simp = simplex.simplex3(i*scale,j*scale,0)
            simplices[key].append(simp)

    #set_trace()

    noise = df(simplices, index=ind)
    noise = (noise + 1) * height
    return noise

def coord_access(frame, coords=(0,0)):
    x = 'X({})'.format(coords[0])
    return frame[x][coords[1]]


noise = generate_map(size=100, scale=.00001)

#print new_noise
#print new_noise.describe()
