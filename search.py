# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
        This class outlines the structure of a search problem, but doesn't implement
        any of the methods (in object-oriented terminology: an abstract class).

        You do not need to change anything in this class, ever.
    """
    def getStartState(self):
        """
                Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
                  state: Search state

                Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
                  state: Search state

                For a given state, this should return a list of triples, (successor,
                action, stepCost), where 'successor' is a successor to the current
                state, 'action' is the action required to get there, and 'stepCost' is
                the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
                 actions: A list of actions to take

                This method returns the total cost of a particular sequence of actions.
                The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def generic_search(problem, strategy, use_cost=False, heuristic=None):      #(R)
    if strategy == "BFS":           #Chooses the frontier based on the Algorithm
        frontier = util.Queue()
    elif strategy == "DFS":
        frontier = util.Stack()
    else:
        frontier = util.PriorityQueue()

    initial = problem.getStartState()       #Initilizes the initial state and the frontier

    if strategy in ["UCS", "A*", "GBS"]:    #Adds the initial state to the frontier
        frontier.push((initial, [], 0), 0)
    else:
        frontier.push((initial, [], 0))

    explored = set()    #Initializing to store the explored nodes
    nodesExpanded = 0   #Counter
    path = []           #Stores the paths visited

    while not frontier.isEmpty():   #Continues until the frontier is empty
        if strategy in ["BFS", "DFS"]:
            currentState, actions, currentCost = frontier.pop()
        else:
            currentState, actions, currentCost = frontier.pop()

        if problem.isGoalState(currentState):            # Check if the current state is the goal state
            path.append((currentState, "Goal Reached"))
            return actions, nodesExpanded, path, len(actions)

        if currentState in explored:        # If this state has already been explored, then skip it
            continue

        explored.add(currentState)        # Mark the current state as explored and increment the counter
        nodesExpanded += 1

        # Finds all the possible actions that can be taken from the current state by taking an action(Successors)
        for (succ, action, pathCost) in problem.getSuccessors(currentState):
            newAction = actions + [action]
            newCost = currentCost + pathCost

            if succ not in explored:    #If not explored, adds the Successor to the frontier
                if strategy in ["UCS", "A*", "GBS"]:
                    priority = newCost
                    if strategy == "A*" and heuristic:
                        priority += heuristic(succ, problem)
                    elif strategy == "GBS" and heuristic:
                        priority += heuristic(succ, problem)
                    frontier.push((succ, newAction, newCost), priority)
                else:
                    frontier.push((succ, newAction, newCost))
                path.append((currentState, action))

    return [], nodesExpanded, path, 0   #Returns empty if there's no solution


def breadthFirstSearch(problem):
    """
    This function implements the Breadth First Search Algorithm
    """
    return generic_search(problem, strategy="BFS")

def depthFirstSearch(problem):
    """
        This function implements the Depth First Search Algorithm
    """
    return generic_search(problem, strategy="DFS")

def uniformCostSearch(problem):
    """
        This function implements the Uniform Cost Search Algorithm
    """
    return generic_search(problem, strategy="UCS", use_cost=True)

def aStarSearch(problem, heuristic):
    """
        This function implements the A* Search Algorithm
        The function also takes in a heuristic depending on the input
    """
    return generic_search(problem, strategy="A*", use_cost=True, heuristic=heuristic)

def greedyBestFirstSearch(problem, heuristic):
    """
        This function implements the A* Search Algorithm
        The function also takes in a heuristic depending on the input
    """
    return generic_search(problem, strategy="GBS", use_cost=True, heuristic=heuristic)

def nullHeuristic(state, problem=None):
    return 0


def misplacedTile(state, problem):
    """
        Heuristic function to count the number of misplaces tiles
    """
    goal = [[1, 2, 3], [8, None, 4], [7, 6, 5]]
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state.cells[i][j] != goal[i][j] and state.cells[i][j] is not None:
                misplaced += 1

    return misplaced


def manhattanDistance(state, problem):
    """
        Heuristic function to calculate the manhattan Distance
    """
    goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2), 8: (1, 0), None: (1, 1), 4: (1, 2), 7: (2, 0), 6: (2, 1), 5: (2, 2)}
    distance = 0

    for i in range(3):
        for j in range(3):
            tile = state.cells[i][j]
            if tile is not None and tile != 0:
                goal_i, goal_j = goal_positions[tile]
                distance += util.manhattanDistance((i, j), (goal_i, goal_j))

    return distance


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
gbfs = greedyBestFirstSearch
astar = aStarSearch
ucs = uniformCostSearch