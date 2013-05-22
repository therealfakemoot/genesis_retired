from genesis import generate_map
from genesis import rescale
from vis import topo
import vis

def demo():
    '''A simple demo of how to use Genesis programatically.'''
    height = 1000
    n = generate_map(750 ,scale=.005)
    n = rescale(n, height)
    topo(n-(height*1/3))
    vis.PLT.show()

if __name__ == '__main__':
    demo()
