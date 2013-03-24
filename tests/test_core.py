from genesis.lib import core
from nose import with_setup

def test_MapGeneration():
    noise = core.generate_map(size=10)


@with_setup(test_MapGeneration)
def test_CoordinateAccess():
    pass
