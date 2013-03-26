from lib.core import generate_map
from lib.vis import topo
import lib.vis as vis

n = generate_map(200, scale=.005, simp=True)
topo(n)
vis.PLT.show()
