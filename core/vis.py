from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP
from core import generate_map
from matplotlib.pyplot import contour

def view(frame, viewport):
    '''
    Returns a windowed version of the dataframe.
    viewport: tuple
        A tuple of the form (x,y,height,width)
    '''
    y,x,h,w = viewport
    return frame.ix[x:x+w,y:y+h], 

def slice(frame, viewport):
    xmax,ymax = frame.size
    y,x,h,w = viewport
    if any(n % 2 != 0 for n in view): raise ValueError('Viewport values must be even integers.')
    chunks = xmax/w
    
        

def topo(noisemap, view=None, levels=None, **kwargs):
    '''Plots a topological map of a given heightmap, with an optional viewport
    for fine grained mapping.

    noisemap: DataFrame
    viewport : tuple,(y,x,h,w)
        A tuple containing the top left corner of the viewport, and the width
        and height. Allows subsections of the map to be displayed.
    '''
    if not levels:
        nmax = int(max(noisemap.max()))
        nmin = int((min(noisemap.min())))
        step = (nmax - nmin)/15
        levels = range(nmin, nmax, step)
    if view:
        con = contour(view(noisemap, view), levels, **kwargs)
    else:
        con = contour(noisemap, levels, **kwargs)
    PLT.clabel(con, inline=1, fontsize=10)
    #CB = PLT.colorbar(con, extend='both')
    return con
