class Junction:
    def __init__(self, north = None, east = None, south = None, west = None):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.pivot = False

class Labyrinth:
    def __init__(self):
        self.start = None
        self.addJunction = self.add_junction
    def add_junction(self, junction):
        if self.start == None:
            self.start = junction


labyrinth = Labyrinth()

