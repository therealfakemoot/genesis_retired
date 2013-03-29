from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP
from core import generate_map
from matplotlib.pyplot import contour

def histo():
    gridsize=100
    PLT.subplot(111)

# if 'bins=None', then color of each hexagon corresponds directly to its count
# 'C' is optional--it maps values to x-y coordinates; if 'C' is None (default) then 
# the result is a pure 2D histogram 
    size = 150
    noise = generate_map(size)
    x = y = NP.array(range(-size,size))
    PLT.hexbin(x, y, C=noise.values, gridsize=gridsize, cmap=CM.jet)
    PLT.axis([x.min(), x.max(), y.min(), y.max()])

    cb = PLT.colorbar()
    cb.set_label('mean value')
    PLT.show()

def view(frame, viewport):
    y,x,h,w = viewport
    return frame.ix[x:x+w,y:y+h], 

def topo(noisemap, view=None, **kwargs):
    '''Plots a topological map of a given heightmap, with an optional viewport
    for fine grained mapping.

    noisemap: DataFrame
    viewport : tuple,(y,x,h,w)
        A tuple containing the top left corner of the viewport, and the width
        and height. Allows subsections of the map to be displayed.
    '''
    if view:
        con = contour(view(noisemap, view), **kwargs)
    else:
        con = contour(noisemap, **kwargs)
    PLT.clabel(con, inline=1, fontsize=10)
    CB = PLT.colorbar(con, extend='both')
    return con
