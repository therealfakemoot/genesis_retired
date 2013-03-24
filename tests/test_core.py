from genesis.lib import core
from nose import with_setup

class test_Core():
    @classmethod
    def setupClass(self):
        self.noise = core.generate_map(size=10)

    def test_MapGeneration(self):
        noise = core.generate_map(size=10)

    def test_CoordinateAccess(self):
        core.coord_access(self.noise)
