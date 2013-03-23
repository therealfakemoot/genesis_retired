import uuid
from collections import defaultdict as ddict

dirs = ('north', 'west', 'northeast', 'northwest', 'southeast', 'southwest', 'east', 'south')
dirs_r = sorted(dirs, reverse=True)
dir_pairs = zip(dirs, dirs_r)

def format_table(table, extra_space=1):
    if not table:
        return [[]]

    max_widths = [max([len(str(val)) for val in col]) for col in table]
    ftable = []
    for irow in range(len(table[0])):
        ftable.append([str(col[irow]).ljust(max_widths[icol]) + " " * extra_space for icol, col in enumerate(table)])
    return ftable

def print_table(table):
    for ir, row in enumarate(table):
        string += "\n" + "".join(row)
        #print string

class Room(object):
    '''This class represents a room in the map. It separates planar exits from non-planar for easy display of two-dimensional maps.''' 
    def __init__(self):
        self.id = str(uuid.uuid4())        
        self.names = ('','')
        self.ends = ()
        self.exits = dict()

class Exit(object):
    def __init__(self, destination, desc, planar =True):
        self.dest = destination #An x,y,z tuple
        self.desc = desc
        self.planar = planar


class Map(object):
    def __init__(self, x = 10, y = 10):
        self.rooms = ddict(Room)
        self._current = None
        self._coords = None

        self.dirs = {'north':(0,1, 0),
                'south':(0,-1, 0),
                'east':(1,0, 0),
                'west':(-1,0, 0),
                'northeast':(1,1, 0),
                'northwest':(-1,1, 0),
                'southeast':(1,-1, 0),
                'southwest':(-1,-1, 0)
        }

        for i in range(x):
            for j in range(y):
                self.rooms[(i,j,0)]

        self.current = (0,0,0) #Initializes a new map's current position to the Origin.
        self._coords = (0,0,0)

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        if isinstance(value, Room):
            self._current = value
        else:
            self._current = self[value]
            self._coords = value

    def __getitem__(self, key):
        try:
            return self.rooms[key]
        except KeyError:
            raise KeyError('The room at the key {} does not exist.'.format(key))

    def __len__(self):
        return len(self.rooms)

    def translate(self, coords, cardinal):
        vector_add = lambda v1, v2: (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

        return vector_add(coords, self.dirs[cardinal])


    def walk(self, direction, planar = True):
        out = self.current.exits.get(direction, None)
        if out:
            self.current = self[out.dest]
        else:
            raise NameError('Exit does not exist.')

    @classmethod
    def neighbors(cls, point1, point2):
        x1,y1,z1 = point1
        x2,y2,z2 = point2
        distance = lambda x,y: abs(max(x,y) - min(x,y))
        if distance(x1,x2) < 2 and distance(y1,y2) < 2 and distance(z1, z2) < 2:
            return True
        else:
            return False

    def dig(self, name):
        origin_room = self.current
        if name in self.dirs:
            dest = self.translate(self._coords, name)
            dest_room = self[dest]
            exit_out = Exit(dest, name, planar = True)
            exit_in = Exit(self._coords, name, planar = True)
        else:
            exit_out = Exit(dest, name, planar = False)
            exit_in = Exit(self._coords, name, planar = True)

        origin_room.exits[name] = exit_out
        dest_room.exits[name] = exit_in
