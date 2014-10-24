import argparse

from genesis.map import Map
from genesis.plot import plot_map

parser = argparse.ArgumentParser(prog='Genesis v.1', description='Genesis World Generation toolkit.')

parser.add_argument('x', metavar='X', type=int, help='The width of the map to be created or plotted.')
parser.add_argument('y', metavar='Y', type=int, help='The height of the map to be created or plotted.')
parser.add_argument('-D', '--demo', action='store_true')

args = parser.parse_args()

if args.demo:
    plot_map(Map((args.x, args.y)))
