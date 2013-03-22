from pandas import DataFrame as df
from lib import simplex
from lib.profiler import profile_this
from random import randint
import sys
from collections import OrderedDict as od
from pdb import set_trace

#@profile_this
def generate_map(size=None, seed=None, scale=None):
    '''Generates a table of simplex values sampled across a two-dimensional plane.'''
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
    return df(simplices, index=ind)


noise = generate_map(size=100, scale=.00001)

noise = (noise + 1) * 500
#print new_noise
#print new_noise.describe()
