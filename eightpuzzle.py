# eightpuzzle.py
# --------------
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


import time
import argparse
import search
import itertools

# Module Classes

class EightPuzzleState:
    """
    The Eight Puzzle is described in the course textbook on
    page 64.

    This class defines the mechanics of the puzzle itself.  The
    task of recasting this puzzle as a search problem is left to
    the EightPuzzleSearchProblem class.
    """

    def __init__( self, numbers ):
        """
                  Constructs a new eight puzzle from an ordering of numbers.

                numbers: a list of integers from 0 to 8 representing an
                  instance of the eight puzzle.  0 represents the blank
                  space.  Thus, the list

                    [1, 0, 2, 3, 4, 5, 6, 7, 8]

                  represents the eight puzzle:
                    -------------
                    | 1 |   | 2 |
                    -------------
                    | 3 | 4 | 5 |
                    -------------
                    | 6 | 7 | 8 |
                    ------------

                The configuration of the puzzle is stored in a 2-dimensional
                list (a list of lists) 'cells'.
        """
        self.cells = []
        numbers = numbers[:] # Make a copy so as not to cause side effects.
        numbers.reverse()
        for row in range( 3 ):
            self.cells.append( [] )
            for col in range( 3 ):
                self.cells[row].append( numbers.pop() )
                if self.cells[row][col] == 0:
                    self.blankLocation = row, col

    def isGoal(self):
        """
                  Checks to see if the puzzle is in its goal state.

                    -------------
                    |   | 1 | 2 |
                    -------------
                    | 3 | 4 | 5 |
                    -------------
                    | 6 | 7 | 8 |
                    -------------

                >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).isGoal()
                True

                >>> EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).isGoal()
                False
        """
        goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]  # Define the goal state
        for row in range(3):
            for col in range(3):
                if self.cells[row][col] != goal[row][col]:
                    return False
        return True

    def legalMoves(self):
        """
                  Returns a list of legal moves from the current state.

                Moves consist of moving the blank space up, down, left or right.
                These are encoded as 'up', 'down', 'left' and 'right' respectively.

                >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).legalMoves()
                ['down', 'right']
        """
        moves = []
        row, col = self.blankLocation
        if row != 0:
            moves.append('up')
        if row != 2:
            moves.append('down')
        if col != 0:
            moves.append('left')
        if col != 2:
            moves.append('right')
        return moves

    def result(self, move):
        """
                  Returns a new eightPuzzle with the current state and blankLocation
                updated based on the provided move.

                The move should be a string drawn from a list returned by legalMoves.
                Illegal moves will raise an exception, which may be an array bounds
                exception.

                NOTE: This function *does not* change the current object.  Instead,
                it returns a new object.
        """
        row, col = self.blankLocation
        if (move == 'up'):
            newrow = row - 1
            newcol = col
        elif (move == 'down'):
            newrow = row + 1
            newcol = col
        elif (move == 'left'):
            newrow = row
            newcol = col - 1
        elif (move == 'right'):
            newrow = row
            newcol = col + 1
        else:
            raise ValueError("Illegal Move")

        # Create a copy of the current eightPuzzle
        newPuzzle = EightPuzzleState([0, 0, 0, 0, 0, 0, 0, 0, 0])
        newPuzzle.cells = [values[:] for values in self.cells]
        # And update it to reflect the move
        newPuzzle.cells[row][col] = self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol] = self.cells[row][col]
        newPuzzle.blankLocation = newrow, newcol

        return newPuzzle

    # Utilities for comparison and display
    def __eq__(self, other):
        """
                    Overloads '==' such that two eightPuzzles with the same configuration
                  are equal.

                  >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]) == \
                      EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).result('left')
                  True
        """
        for row in range(3):
            if self.cells[row] != other.cells[row]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.cells))

    def __getAsciiString(self):
        """
          Returns a display string for the maze
        """
        lines = []
        horizontalLine = ('-' * (13))
        lines.append(horizontalLine)
        for row in self.cells:
            rowLine = '|'
            for col in row:
                if col == 0:
                    col = ' '
                rowLine = rowLine + ' ' + col.__str__() + ' |'
            lines.append(rowLine)
            lines.append(horizontalLine)
        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()


class EightPuzzleSearchProblem(search.SearchProblem):
    """
      Implementation of a SearchProblem for the  Eight Puzzle domain

      Each state is represented by an instance of an eightPuzzle.
    """

    def __init__(self,puzzle):
        "Creates a new EightPuzzleSearchProblem which stores search information."
        self.puzzle = puzzle

    def getStartState(self):
        return self.puzzle

    def isGoalState(self,state):
        return state.isGoal()

    def getSuccessors(self, state):
        """
                  Returns list of (successor, action, stepCost) pairs where
                  each succesor is either left, right, up, or down
                  from the original state and the cost is 1.0 for each
        """
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        """
                 actions: A list of actions to take

                This method returns the total cost of a particular sequence of actions.  The sequence must
                be composed of legal moves
        """
        return len(actions)


searchCompare = []     # Global list to store the Search Comparison results


def parseValue(temp):
    """
    Parses a 2D list from command-line input
    """
    state = eval(temp.replace("-", "0"))  # Replace '-' with '0'    (R)
    result = list(itertools.chain(*state))  # Flatten the 2D list (R)
    return result


def runSearch(algorithm, problem, heuristic=None):
    """
    Runs the search algorithm and returns the result.
    """
    startTime = time.time()

    #Based on the user input, the function will run the requested algorithm
    if algorithm == "BFS":
        result, nodesExpanded, path, depth = search.breadthFirstSearch(problem)
    elif algorithm == "DFS":
        result, nodesExpanded, path, depth = search.depthFirstSearch(problem)
    elif algorithm == "UCS":
        result, nodesExpanded, path, depth = search.uniformCostSearch(problem)
    elif algorithm == "GBS":
        result, nodesExpanded, path, depth = search.greedyBestFirstSearch(problem, heuristic)
    elif algorithm == "A*":
        result, nodesExpanded, path, depth = search.aStarSearch(problem, heuristic)

    endTime = time.time()
    timeTaken = endTime - startTime #Calcultes the tame taken to solve the problem
    cost = problem.getCostOfActions(result) #Calcultes the path cost to solve the problem
    return path, cost, depth, timeTaken, nodesExpanded


def searchValues(algorithm, heuristic, cost, depth, timeTaken, nodesExpanded):
    """
    Stores the Search results to be displayed in the comparison table
    """
    searchCompare.append({
        'Algorithm': algorithm,
        'Heuristic': heuristic if heuristic else "N/A",
        'Path Cost': cost,
        'Depth': depth,
        'Time Taken': f"{timeTaken:.4f} sec",
        'Nodes Expanded': nodesExpanded
    })


def solPath(path):
    """
    The function will format the search path for output
    """
    sol = []
    for state, action in path:
        sol.append(f"[State: {state.cells}    Action: {action}]")
    return "\n".join(sol)


def printOutput(algorithm, path, cost, depth, timeTaken, nodesExpanded, outputFile):
    """
    Prints the Search results to the output file.
    """
    with open(outputFile, "w") as file:
        file.write(f"{algorithm} Search Algorithm:\n")
        file.write("******************************\n")
        file.write(f"Solution Path:\n{solPath(path)}\n")
        file.write(f"Path Cost: {cost}\n")
        file.write(f"Depth: {depth}\n")
        file.write(f"Time Taken: {timeTaken:.4f} seconds\n")
        file.write(f"Nodes Expanded: {nodesExpanded}\n")
        file.write("******************************\n")


def searchTable(outputFile="output.txt"):
    """
    Prints the comparison table to the output file.
    """
    with open(outputFile, "a") as file:
        file.write("\nSearch Algorithms Comparison Table:\n")
        file.write("Algorithm | Heuristic | Path Cost | Depth     | Time Taken | Nodes Expanded\n")
        file.write("------------------------------------------------------------------------------\n")
        for result in searchCompare:
            file.write(
                f"{result['Algorithm']:<9} | {result['Heuristic']:<9} | {result['Path Cost']:<9} | {result['Depth']:<9} | {result['Time Taken']:<9} | {result['Nodes Expanded']:<9}\n")
        file.write("------------------------------------------------------------------------------\n")


def parseInput():
    """
    Parses the command-line arguments
    """
    parser = argparse.ArgumentParser(
        prog="8-Puzzle-Problem",
        description="Solve 8-puzzle using various search algorithms")
    parser.add_argument("--search", type=str, required=True,
                        help="Search algorithm")
    parser.add_argument("--heuristic", type=str,
                        help="Heuristic function")
    parser.add_argument("--initial", type=str, required=True,
                        help="Initial puzzle state")
    parser.add_argument("--goal", type=str, required=True,
                        help="Goal puzzle state")
    return parser.parse_args()


def searchFile(search_algorithm, heuristic):
    """
    Generates the output file specific to the Search Algorithm requested.
    """
    if heuristic:
        return (f"output_{search_algorithm}_{heuristic}.txt")
    else:
        return (f"output_{search_algorithm}.txt")

def main():
    """
       Main function where we run the Search Algorithms
    """
    args = parseInput()

    initial = parseValue(args.initial)  #Parses the initial and goal states from the input
    goal = parseValue(args.goal)

    problem = EightPuzzleSearchProblem(EightPuzzleState(initial))   #Creates a search problem taking the initial state of the Puzzle

    path, cost, depth, timeTaken, nodesExpanded = None, None, None, None, None #Initilizing the variables to store the results

    searchAlg = [   #All the search Algorithms available for this problem with their heuristics
        ("BFS", None),
        ("DFS", None),
        ("UCS", None),
        ("GBS", search.misplacedTile),
        ("GBS", search.manhattanDistance),
        ("A*", search.misplacedTile),
        ("A*", search.manhattanDistance),
    ]

    selected_algorithm = args.search    #Chooses the appropriate Algorithm along with the heuristic depending on the input
    selected_heuristic = search.misplacedTile \
        if args.heuristic == "misplaced" \
        else search.manhattanDistance \
        if args.heuristic == "manhattan" \
        else None

    path, cost, depth, timeTaken, nodesExpanded = runSearch(selected_algorithm, problem, selected_heuristic) #Runs the algorithms and stores the results in these variables
    searchValues(selected_algorithm, args.heuristic if selected_heuristic else None, cost, depth, timeTaken, nodesExpanded) #This will be used for the Comparison table

    outputFile = searchFile(selected_algorithm, args.heuristic) #Generates the specific output file
    printOutput(selected_algorithm, path, cost, depth, timeTaken, nodesExpanded, outputFile)

    #Runs the remaining Search Algorithms for the Comparison Table
    for algorithm, heuristic in searchAlg:
        heuristic_name = "misplaced" if heuristic == search.misplacedTile else "manhattan" if heuristic == search.manhattanDistance else None
        if algorithm == selected_algorithm and heuristic_name == args.heuristic:
            continue        # Skip the algorithm that was already run

        path, cost, depth, timeTaken, nodesExpanded = runSearch(algorithm, problem, heuristic)
        searchValues(algorithm, heuristic_name, cost, depth, timeTaken, nodesExpanded)

    searchTable()   #Calls to output the table


if __name__ == "__main__":
    main()


