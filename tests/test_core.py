from genesis.core import genesis

class test_Core():
    @classmethod
    def setupClass(self):
        self.noise = genesis.generate_map(size=10)

    def test_MapGeneration(self):
        noise = genesis.generate_map(size=10)

    def test_CoordinateAccess(self):
        genesis.coord_access(self.noise)
