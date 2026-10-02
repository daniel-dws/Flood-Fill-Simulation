#Constant definitions
DIRS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}

OPP_DIRS = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

class Maze:
    def __init__(self, size):
        self.size = size
        self.walls = {}
        for x in range(size):
            for y in range(size):
                self.walls[(x, y)] = set() 

        for i in range(size):
            self.add_wall(i, 0, "N")
            self.add_wall(i, size-1, "S")
            self.add_wall(0, i, "W")
            self.add_wall(size-1, i, "E")

    def neighbors(self, x, y):
        result = []
        for side in DIRS:
            if not self.has_wall(x, y, side):
                dx, dy = DIRS[side]
                result.append((x+dx, y+dy))
        return result

    def add_wall(self, x, y, side):
        self.walls[(x, y)].add(side)
        dx, dy = DIRS[side]
        nx, ny = x + dx, y + dy
        if (0 <= nx < self.size and 0 <= ny < self.size):
            self.walls[(nx, ny)].add(OPP_DIRS[side])

    def has_wall(self, x, y, side):
        return side in self.walls[(x, y)]

    #Test
m = Maze(4)
print(m.neighbors(0, 0))      # [(1, 0), (0, 1)]
m.add_wall(1, 1, "E")
print(m.has_wall(1, 1, "E"))  # True
print(m.has_wall(2, 1, "W"))  # True
print(m.neighbors(1, 1))      # no (2, 1) in the list
