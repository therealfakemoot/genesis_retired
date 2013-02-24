from mapper.lib.objects import Map, Room, Exit
from mapper.lib.objects import dirs as Cardinals
from nose.tools import raises

def test_RoomCreation():
    new_map = Map(3, 3)
    assert len(new_map) == 9

def mapMove(new_map, direction):
    new_map.walk(direction)

def test_PlanarMapMovementWithoutExits():
    new_map = Map(3,3)
    new_map.current = (1,1,1)
    for exit in Cardinals:
        yield raises(NameError)(mapMove), new_map, exit 

def test_CreatePlanarExits():
    new_map = Map(4,4)
    new_map.current = (1,1,1)
    for exit in Cardinals:
        yield new_map.dig, exit

def test_PlanarMapMovementWithExits():
    new_map = Map(4,4)
    new_map.current = (1,1,1)
    for exit in Cardinals:
        new_map.dig(exit)
    for exit in Cardinals:
        yield mapMove, new_map, exit
        new_map.current = (1,1,1)

#def test_MapLocationFollow():
    #This test should make sure that the map will keep track of the current location when given movement commands.
    #pass



'''
def planarExitTest(origin, dest, ind):
    assert origin.exits[ind] is dest.exits[ind]

def test_JoinPlanarRooms():
    new_map = dummy_map(4,4)
    origin_room = (1,1,0)
    dirs = (('west','east'),('south','north'),('southwest','southeast'),('northeast','northwest'),('east','west'),('north','south'),('southeast','southwest'),('northwest','northeast'))
    for coming, going in dirs:
        Map.join(origin_room, (coming, going))

def test_JoinNonPlanarRooms():
    new_room = Room()
    adjacent_room = Room()
    desc = ('stairs', 'stairs')
    Map.join(new_room, adjacent_room, desc, planar = False)

    assert new_room.np_exits[0] is adjacent_room.np_exits[0]

def test_MapNeighborsCheck():
    assert Map.neighbors((0,0,0),(0,1,0)) == True and Map.neighbors((0,0,0),(0,10,0)) == False and Map.neighbors((0,0,0),(10,0,0)) == False
    '''
