import logging
import argparse

from genesis.map import Map
from genesis.plot import plot_map


def logging_config():
    logger = logging.getLogger('')

    fh = logging.FileHandler('genesis.log')
    fh.setlevel(logging.INFO)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    logger.addHandler(ch)


def demo(args):
    plot_map(Map((args.x, args.y)))


def main(args=None):
    parser = argparse.ArgumentParser(prog='Genesis v.1', description='Genesis World Generation toolkit.')

    parser.add_argument('x', metavar='X', type=int, help='The width of the map to be created or plotted.')
    parser.add_argument('y', metavar='Y', type=int, help='The height of the map to be created or plotted.')
    parser.add_argument('-D', '--demo', action='store_true')

    args = parser.parse_args()

    if args.demo:
        demo(args)
