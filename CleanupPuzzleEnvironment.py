from ipythonblocks import BlockGrid
from agents import *

class CleanupPuzzleEnvironment(Environment):
    def __init__(self, width=5, height=5):
        super(CleanupPuzzleEnvironment, self).__init__()
        self.width = width
        self.height = height

        self.bg_color = (207, 216, 220)
        self.ball_color = (0, 191, 165)
        self.click_color = (244, 67, 54)
        self.grid = BlockGrid(width, height, fill=self.bg_color)

    def __str__(self):
        world = self.get_world()
        self.draw_grid(world)
        self.grid.show()
        return ''

    def draw_grid(self, world):
        self.grid[:] = self.bg_color
        for x in range(0, len(world)):
            for y in range(0, len(world[x])):
                if len(world[x][y]) and isinstance(world[x][y][0], Ball):
                    self.grid[x, y] = self.ball_color
                elif len(world[x][y]) and isinstance(world[x][y][0], Click):
                    self.grid[x, y] = self.click_color

    def get_world(self):
        '''returns the items in the world'''
        result = []
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append(self.list_things_at((x, y)))
            result.append(row)
        return result

    def is_inbounds(self, location):
        '''Checks to make sure that the location is inbounds'''
        x,y = location
        return not (x < 0 or x >= self.height or y < 0 or y >= self.width)

