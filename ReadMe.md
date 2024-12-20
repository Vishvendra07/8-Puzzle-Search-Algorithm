# 8-Puzzle Search Algorithms Project

## Overview

This project implements a variety of search algorithms to solve the 8-puzzle problem. The project compares the performance of these algorithms in terms of the following metrics:
- Path cost (the total cost of reaching the goal state)
- Search depth (how deep in the tree the goal was found)
- Time taken (execution time of the algorithm)
- Number of expanded nodes (how many nodes were explored during the search)

The implemented search algorithms include:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Uniform Cost Search (UCS)**
- **Greedy Best-First Search (GBS)** with the following heuristics:
  - Misplaced tiles heuristic
  - Manhattan distance heuristic
- **A* Search (A*)** with the following heuristics:
  - Misplaced tiles heuristic
  - Manhattan distance heuristic

The project outputs performance results for these algorithms, compares their efficiency, and generates a table summarizing the metrics.

## Project Structure

The project consists of the following files:

- **eightpuzzle.py**: Implements the 8-puzzle problem, defines legal moves, and interacts with the search algorithms to find a solution.
- **search.py**: Contains the core search algorithms (BFS, DFS, UCS, GBS, A*) and heuristic functions.
- **util.py**: Contains the utilities which can be used for the project
- **README.md**: This documentation file.
- **output.txt**: A file where the results of the all the search algorithms are stored. Each search algorithm outputs the path cost, depth, time taken, and number of nodes expanded and are compared.
- **output_{search}_{heuristic}.txt**: A file where the results of the requested search algorithm is stored. The Search algorithm outputs the Solution path, path cost, depth, time taken, and number of nodes expanded.

## Problem Statement

The 8-puzzle problem consists of a 3x3 grid containing tiles numbered from 1 to 8, with one blank space represented by `0`. The objective is to rearrange the tiles from a given initial state to match a specified goal state by sliding the tiles into the blank space using the least number of moves.

The program uses search algorithms to find the shortest path from the initial state to this goal state, while keeping track of the cost and efficiency of each algorithm.

This is the **initial** state: **[[0, 2, 3], [1, 4, 5], [8, 7, 6]]**

And this is the **goal** state: **[[1, 2, 3], [8, 0, 4], [7, 6, 5]]**


## Main Functionality

The `eightpuzzle.py` script is the main program that solves the 8-puzzle problem using various search algorithms. It accepts inputs for the search algorithm, heuristic function , and the initial and goal states of the puzzle. The results, including path cost, search depth, time taken, and nodes expanded, are printed in output files.

### Main Functions

#### `runSearch(algorithm, problem, heuristic=None)`
This is the main function responsible for running the specified search algorithm on the 8-puzzle problem. The function returns the solution path, path cost, depth of the solution, time taken to find the solution, and the number of expanded nodes.

#### `searchValues(algorithm, heuristic, cost, depth, timeTaken, nodesExpanded)`
This helper function stores the search results (algorithm name, heuristic, path cost, depth, time taken, and nodes expanded) in a global list `searchCompare`, which is used to generate a comparison table for the algorithms.

#### `solPath(path)`
This helper function formats the solution path. It is used to print the solution.


#### `printOutput(algorithm, path, cost, depth, timeTaken, nodesExpanded, outputFile)`
This function writes the search results to an output file. The file will contain details about the search algorithm used, the solution path, path cost, search depth, time taken, and number of nodes expanded.


#### `searchTable(outputFile="output.txt")`
This function generates a comparison table summarizing the results of different search algorithms (e.g., BFS, DFS, UCS, A*, GBS) and writes the table to an output file. It includes columns for the algorithm, heuristic, path cost, depth, time taken, and number of nodes expanded.


## Search Algorithms

In `search.py`, various search algorithms are implemented to work with the 8-puzzle problem.

### Generic Search Function

#### `generic_search(problem, strategy, use_cost=False, heuristic=None)`
This is a generic search function that handles multiple search strategies (BFS, DFS, UCS, A*, GBS) based on the given parameters. The function selects the appropriate search strategy (queue, stack, or priority queue) and applies the algorithm to find the solution.

#### `breadthFirstSearch(problem)`
This function implements the Breadth-First Search (BFS) algorithm, which explores all nodes at the current depth level before moving on to nodes at the next depth level.

#### `depthFirstSearch(problem)`
This function implements the Depth-First Search (DFS) algorithm, which explores as far as possible along a branch before backtracking.

#### `uniformCostSearch(problem)`
This function implements Uniform Cost Search (UCS), which expands the node with the lowest path cost, ensuring the least-cost solution is found.

#### `aStarSearch(problem, heuristic)`
This function implements A* search, which uses both the path cost (`g(n)`) and the heuristic function (`h(n)`) to find the optimal solution.

#### `greedyBestFirstSearch(problem, heuristic)`
This function implements Greedy Best-First Search (GBS), which expands the node that appears closest to the goal based solely on the heuristic function.

### Heuristic Functions

#### `misplacedTile(state, problem)`
This heuristic function calculates the number of misplaced tiles compared to the goal state. It is used by A* and GBS to estimate how far the current state is from the goal.


#### `manhattanDistance(state, problem)`
This heuristic function calculates the sum of the Manhattan distances of each tile from its goal position. It provides a more accurate estimate of the distance to the goal than the misplaced tiles heuristic.

---

## Requirements

- **Python 3**: Ensure that you have Python installed. The code is compatible with Python 3.
- **`util.py` file**: This file contains utility functions like Queue, Stack, and PriorityQueue, which are used to implement search algorithms. You must have this file in the same directory as `eightpuzzle.py` and `search.py`.

## Setup

1. Clone or download this repository or project to your local machine.
   
2. Ensure you have the required files including the `util.py` file.

3. Open a terminal and navigate to the directory where the project files are stored.

## Running the Code

### Basic Syntax

To run the 8-puzzle search program, use the following command:

```bash
python eightpuzzle.py –search “DFS/BFS/UCS/GBS/A*” –initial ‘[[-,2,3],[1,4,5],[8,7,6]]’ –goal ‘[[1,2,3],[8,-,4],[7,6,5]]’ –heuristic “misplaced/manhattan/other”

python eightpuzzle.py --search "A*" --initial "[[-,2,3],[1,4,5],[8,7,6]]" --goal "[[1,2,3],[8,-,4],[7,6,5]]" --heuristic manhattan

python eightpuzzle.py --search DFS --initial "[[-,2,3],[1,4,5],[8,7,6]]" --goal "[[1,2,3],[8,-,4],[7,6,5]]"



