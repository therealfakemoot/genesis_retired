from core.genesis import generate_map
from core.genesis import rescale
from core.vis import topo
import core.vis as vis
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('create')

parser.add_argument('-l','--load', action='store_false')

parser.add_argument('--size')
parser.add_argument('--scale')
parser.add_argument('--height')


def demo():
    n = generate_map(500,scale=.005)
    n = rescale(n, 7500)
    topo(n)
    vis.PLT.show()

if __name__ == '__main__':
    demo()
