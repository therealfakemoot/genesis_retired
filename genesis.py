from core.genesis import generate_map
from core.genesis import rescale
from core.vis import topo
from core import demo
import core.vis as vis
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--nosave',help='Prevents Genesis from serializing the generated map to disk.', action='store_true')

parser.add_argument('-l','--load', action='store_false')

parser.add_argument('--size')
parser.add_argument('--scale')
parser.add_argument('--height')



if __name__ == '__main__':
    args = parser.parse_args()
    if args.demo:
        demo.demo()
