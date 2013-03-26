from genesis.lib.core import generate_map
from genesis.lib.vis import topo
import genesis.lib.vis as vis
import sys

n = generate_map(int(sys.argv[1]), scale=int(sys.argv[2]), simp=True)
topo(n)
vis.PLT.show()
