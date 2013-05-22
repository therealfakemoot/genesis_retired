from genesis.core.objects import Map, Room, Exit
from genesis.core.objects import dirs as Cardinals
from nose.tools import raises, eq_


class testMap():

    def mapMove(self, new_map, direction):
        new_map.walk(direction)

    def test_RoomCreation(self):
        new_map = Map(3, 3)
        assert len(new_map) == 9

    def test_PlanarMapMovementWithoutExits(self):
        new_map = Map(3,3)
        new_map.current = (1,1,1)
        for exit in Cardinals:
            yield raises(NameError)(self.mapMove), new_map, exit 

    def test_CreatePlanarExits(self):
        new_map = Map(4,4)
        new_map.current = (1,1,1)
        for exit in Cardinals:
            yield new_map.dig, exit

    def test_PlanarMapMovementWithExits(self):
        new_map = Map(4,4)
        new_map.current = (1,1,1)
        for exit in Cardinals:
            new_map.dig(exit)
        for exit in Cardinals:
            yield self.mapMove, new_map, exit
            new_map.current = (1,1,1)


    def test_MapNeighborsCheck(self):
        assert Map.neighbors((0,0,0),(0,1,0)) == True and Map.neighbors((0,0,0),(0,10,0)) == False and Map.neighbors((0,0,0),(10,0,0)) == False
