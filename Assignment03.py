from CleanupPuzzleEnvironment import CleanupPuzzleEnvironment

from agents import *
from Objects import *

from search import ( # Bases for problem building
    Problem, Node, Graph, UndirectedGraph,
    SimpleProblemSolvingAgentProgram,
    GraphProblem
)

from search import ( # Uninformed search algorithms
    tree_search, graph_search, best_first_graph_search,
    breadth_first_tree_search, breadth_first_search,
    depth_first_tree_search, depth_first_graph_search,
    depth_limited_search, iterative_deepening_search,
    uniform_cost_search,
    compare_searchers
)

from search import ( # Informed search algorithms
    greedy_best_first_graph_search, astar_search
)

class CleanBoardProblem(Problem):
    def __init__(self, initial=[], goal=[], size=5):
        Problem.__init__(self, initial, goal)
        self.size = size

    def actions(self, state):
        action_coords = []

        for (x, y) in state:
            near_locations = [(x-1, y), (x+1, y), (x,y-1), (x, y+1)]
            for loc in near_locations:
                if self.is_inbounds(loc) and loc not in state and loc not in action_coords:
                    action_coords.append(loc)

        sorted_list = sorted(action_coords, key=lambda x: [x[0], x[1]])
        return tuple(sorted_list)

    def result(self, state, action):
        x, y = action
        near_locations = [(x-1, y), (x+1, y), (x,y-1), (x, y+1)]

        new_state = [e for e in state]
        for loc in near_locations:
            if self.is_inbounds(loc) and loc not in new_state:
                new_state.append(loc)
            elif self.is_inbounds(loc) and loc in new_state:
                new_state.remove(loc)

        sorted_list = sorted(new_state, key=lambda x: [x[0], x[1]])
        return tuple(sorted_list)

    def goal_test(self, state):
        if len(state) < 1:
            return True
        return False

    def path_cost(self, c, state1, action, state2):
        diff = len(state2) - len(state1)
        return c + diff

    def is_inbounds(self, location):
        '''Checks to make sure that the location is inbounds'''
        x,y = location
        return not (x < 0 or x >= self.size or y < 0 or y >= self.size)

if __name__ == "__main__":
    initial_state = tuple([(0,0), (1,1), (2,0), (3,3), (4,2), (4,4)])
    size = 5

    # initial_state = [(0,3), (1,2), (1,4), (2,3), (3,7), (4,6), (4,3), (5,2), (5,4), (6,3), (5,9), (6,8), (6,9), (7,8), (7,10), (8,0), (8,5), (8,9), (9,1), (9,4), (9,6), (10,0), (10,5)]
    initial_state = sorted(initial_state, key=lambda x: [x[0], x[1]])
    initial_state = tuple(initial_state)

    problem = CleanBoardProblem(initial_state, [], size)
    # problem.result(initial_state, (0,1))

    problem = CleanBoardProblem(initial_state, [], size)
    goal1 = uniform_cost_search(problem)
