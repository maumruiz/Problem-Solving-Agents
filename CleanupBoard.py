# Implement a class to solve the problem of "Missionaries and Cannibals"
# It includes examples of its use to solve it using the Breadth-first
# algorithm
#
# Author: Dr. Santiago Enrique Conant Pablos
# Date: August 24, 2016

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

class CleanBoard(Problem):

    """The problem of missionaries and cannibals.
        State: (# Missionaries on side 1, # Cannibals on side 1, Boat side) 
        the number of missionaries and cannibals involved can be established"""

    def __init__(self, initial=((1,0,0,0,0),(0,1,0,0,0),(1,0,0,0,0),(0,0,0,1,0),(0,0,1,0,1)), goal=((1,0,0,0,0),(0,1,0,0,0),(1,0,0,0,0),(0,0,0,1,0),(0,0,1,0,1)), myc=3):
        Problem.__init__(self, initial, goal)
        self.misycan = myc # No. of missionaries = No. of cannibals
        self.all_actions = ['M1M','M2M','M1C','M2C','M1M1C'] # possible actions

    def actions(self, state):
        "They depend on the distribution of missionaries and cannibals."
        actions = []
        for action in self.all_actions:
            if action == 'M1M' and \
               not illegal_state(new_state(state,1,0), self.misycan):
                actions.append('M1M')
            elif action == 'M2M' and \
                 not illegal_state(new_state(state,2,0), self.misycan):
                actions.append('M2M')
            elif action == 'M1C' and \
                 not illegal_state(new_state(state,0,1), self.misycan):
                actions.append('M1C')
            elif action == 'M2C' and \
                 not illegal_state(new_state(state,0,2), self.misycan):
                actions.append('M2C')
            elif action == 'M1M1C' and \
                 not illegal_state(new_state(state,1,1), self.misycan):
                actions.append('M1M1C')
        return actions

    def result(self, state, action):
        """The result is calculated by adding or subtracting missionaries 
            and/or cannibals."""
        if action == 'M1M':
            return new_state(state,1,0)
        elif action == 'M2M':
            return new_state(state,2,0)
        elif action == 'M1C':
            return new_state(state,0,1)
        elif action == 'M2C':
            return new_state(state,0,2)
        elif action == 'M1M1C':
            return new_state(state,1,1)

    def h(self, node):
        "heuristic = difference between goal and current status"
        amis, acan, al = node.state
        gmis, gcan, gl = self.goal
        return abs(gmis-amis) + abs(gcan-acan) + abs(gl-al)

def new_state(state, mis, can):
    """Moves mis missionaries and can cannibals to get a new state.
    The resulting state is not verified (may be invalid)"""
    nstate = list(state)
    if nstate[2] == 0:
        nstate[2] = 1
    else:
        mis = - mis
        can = - can
        nstate[2] = 0
    nstate[0] = nstate[0] + mis
    nstate[1] = nstate[1] + can
    return tuple(nstate)
    
def illegal_state(state, misycan):
    """Determine if a state is illegal"""
    return state[0] < 0 or state[0] > misycan or \
           state[1] < 0 or state[1] > misycan or \
           (state[0] > 0 and state[0] < state[1]) or \
           (state[0] < misycan and state[0] > state[1])

def display_solution(goal_node):
    """Displays the sequence of states and actions of a solution"""
    actions = goal_node.solution()
    nodes = goal_node.path()
    print('SOLUTION')
    print('State:',nodes[0].state)
    for na in range(len(actions)):
        if actions[na] == 'M1M':
            print('Action: move one missionary')
        if actions[na] == 'M2M':
            print('Action: move two missionaries')
        if actions[na] == 'M1C':
            print('Action: move one cannibal')
        if actions[na] == 'M2C':
            print('Action: move two cannibals')
        if actions[na] == 'M1M1C':
            print('Action: move one missionary and one cannibal')
        print('State:',nodes[na+1].state)
    print('END')

#-------------------------------------------------------------------
# EJEMPLOS DE USO

# Problem 1: (3,3,1) -> (0,0,0) for 3 missionaries and 3 cannibals
prob1 = CleanBoard(
    (
        (1,0,0,0,0),
        (0,1,0,0,0),
        (1,0,0,0,0),
        (0,0,0,1,0),
        (0,0,1,0,1)
    ),
    (
        (0,0,0,0,0),
        (0,0,0,0,0),
        (0,0,0,0,0),
        (0,0,0,0,0),
        (0,0,0,0,0)
    )
        )
# # Problem 2: (2,2,0) -> (0,0,1) for 3 missionaries and 3 cannibals
# prob2 = CleanBoard((2,2,0),(0,0,1))
# # Problem 3: (4,4,1) -> (2,2,0) for 4 missionaries and 4 cannibals
# prob3 = CleanBoard((4,4,1),(2,2,0),4)
# # Problem 4: (6,5,1) -> (6,0,0) for 6 missionaries and 6 cannibals
# prob4 = CleanBoard((6,5,1),(6,0,0),6)

# Solving the problem 1:
print("Solution of Problem 1 through Breadth-first search")
goal1 = breadth_first_search(prob1)
if goal1:
    display_solution(goal1)
else:
    print("Failure: no solution found")

# Solving the problem 2:
print("Solution of Problem 2 through Breadth-first search")
goal2 = breadth_first_search(prob2)
if goal2:
    display_solution(goal2)
else:
    print("Failure: no solution found")

# Solving the problem 3:
print("Solution of Problem 3 through Breadth-first search")
goal3 = breadth_first_search(prob3)
if goal3:
    display_solution(goal3)
else:
    print("Failure: no solution found")

# Solving the problem 4:
print("Solution of Problem 4 through Breadth-first search")
goal4 = breadth_first_search(prob4)
if goal4:
    display_solution(goal4)
else:
    print("Failure: no solution found")

