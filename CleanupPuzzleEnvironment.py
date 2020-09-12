from ipythonblocks import BlockGrid
from aima import *

class CleanupPuzzleEnvironment(Environment):
    def __init__(self, width=11, height=11):
        super(CleanupPuzzleEnvironment, self).__init__()
        self.width = width
        self.height = height
        self.grid = BlockGrid(width, height, fill=(123, 234, 123))

    def __str__(self):
        world = self.get_world()
        self.draw_grid(world)
        self.grid.show()
        return ''

    def draw_grid(self, world):
        self.grid[:] = (123, 234, 123)
        for x in range(0, len(world)):
            for y in range(0, len(world[x])):
                if len(world[x][y]):
                    self.grid[y, x] = (77,182,172)

    def get_world(self):
        '''returns the items in the world'''
        result = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(self.list_things_at((x, y)))
            result.append(row)
        return result

