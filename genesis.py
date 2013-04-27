from core.genesis import generate_map
from core.genesis import rescale
from core.vis import topo
from core import demo
import core.vis as vis
import sys
import argparse

parser = argparse.ArgumentParser()

map_opts = parser.add_argument_group('Map Properties', 'These arguments relate to the attributes of map generation.')

map_opts.add_argument('--size', help='Desired size of the generated world in terms of pixels.')
map_opts.add_argument('--scale', help='A float that determines the \'smoothness\' of the noisemap. Smaller values create more smoothness.')
map_opts.add_argument('--height', help='Maximum height of the topological map. Units are arbitrary; this value is up for interpretation by the end user.')

save_opts = parser.add_argument_group('Save Options', 'These arguments dictate when, where, and if data is saved to or read from the disk.')
save_opts.add_argument('--nosave',help='Prevents Genesis from serializing the generated map to disk.', action='store_true')
save_opts.add_argument('-l','--load', action='store_false', dest='load', help='Path to a previously serialised noisemap.')


if __name__ == '__main__':
    args = parser.parse_args()
