from core.genesis import generate_map
from core.genesis import rescale
from core.vis import topo
import core.vis as vis
import sys

def main():
    n = generate_map()
    topo(n)
    vis.PLT.show()
