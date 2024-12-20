# 8-Puzzle Search Algorithms Project

## Overview

This project implements various search algorithms to solve the 8-puzzle problem, comparing their performance in terms of:
- Path cost (total cost to reach the goal state)
- Search depth (tree depth where the goal is found)
- Execution time
- Number of expanded nodes

### Implemented Algorithms

1. **Breadth-First Search (BFS)**
2. **Depth-First Search (DFS)**
3. **Uniform Cost Search (UCS)**
4. **Greedy Best-First Search (GBS)**
   - Misplaced tiles heuristic
   - Manhattan distance heuristic
5. **A* Search (A*)**
   - Misplaced tiles heuristic
   - Manhattan distance heuristic

---

## Problem Statement

The 8-puzzle problem involves arranging tiles in a 3x3 grid to match a specified goal state by sliding the tiles into an empty space. 

- **Initial state**: `[[0, 2, 3], [1, 4, 5], [8, 7, 6]]`
- **Goal state**: `[[1, 2, 3], [8, 0, 4], [7, 6, 5]]`

---

## Project Structure

1. **`eightpuzzle.py`**: Defines the 8-puzzle mechanics and interactions with search algorithms.
2. **`search.py`**: Implements search algorithms like BFS, DFS, UCS, A*, and GBS.
3. **`util.py`**: Provides utility functions for data structures (e.g., stacks, queues).
4. **`output.txt`**: Summarizes the performance of all algorithms.
5. **`output_{search}_{heuristic}.txt`**: Logs detailed results of specific algorithm runs.

---

## Usage

### Command Format
```bash
python eightpuzzle.py --search <algorithm> --initial <initial_state> --goal <goal_state> [--heuristic <heuristic>]
```

### Example Commands

#### Breadth-First Search
```bash
python eightpuzzle.py --search BFS --initial "[[0,2,3],[1,4,5],[8,7,6]]" --goal "[[1,2,3],[8,0,4],[7,6,5]]"
```

#### A* Search with Manhattan Heuristic
```bash
python eightpuzzle.py --search A* --initial "[[0,2,3],[1,4,5],[8,7,6]]" --goal "[[1,2,3],[8,0,4],[7,6,5]]" --heuristic manhattan
```

---

## Key Functions

### In `eightpuzzle.py`

- **`runSearch(algorithm, problem, heuristic=None)`**: Executes the specified search algorithm.
- **`searchValues(algorithm, heuristic, cost, depth, timeTaken, nodesExpanded)`**: Logs search results.
- **`printOutput(algorithm, path, cost, depth, timeTaken, nodesExpanded, outputFile)`**: Saves results to an output file.
- **`searchTable(outputFile="output.txt")`**: Generates a performance comparison table for all algorithms.

### In `search.py`

- **`generic_search(problem, strategy, use_cost=False, heuristic=None)`**: Core logic for multiple search strategies.
- **`breadthFirstSearch(problem)`**: Implements BFS.
- **`depthFirstSearch(problem)`**: Implements DFS.
- **`uniformCostSearch(problem)`**: Implements UCS.
- **`aStarSearch(problem, heuristic)`**: Implements A*.
- **`greedyBestFirstSearch(problem, heuristic)`**: Implements GBS.

### Heuristics

- **`misplacedTile(state, problem)`**: Counts the number of misplaced tiles.
- **`manhattanDistance(state, problem)`**: Calculates the Manhattan distance of tiles from their goal positions.

---

## Performance Comparison

| Algorithm   | Heuristic       | Path Cost | Depth | Time Taken | Nodes Expanded |
|-------------|-----------------|-----------|-------|------------|-----------------|
| DFS         | N/A             | 428       | 428   | 0.0074 sec | 435             |
| BFS         | N/A             | 6         | 6     | 0.0006 sec | 58              |
| UCS         | N/A             | 6         | 6     | 0.0006 sec | 58              |
| GBS         | Misplaced Tile  | 6         | 6     | 0.0001 sec | 6               |
| GBS         | Manhattan       | 6         | 6     | 0.0001 sec | 6               |
| A*          | Misplaced Tile  | 6         | 6     | 0.0001 sec | 6               |
| A*          | Manhattan       | 6         | 6     | 0.0001 sec | 6               |

---

## References

1. [Python Argparse Documentation](https://docs.python.org/3/library/argparse.html)
2. [GeeksforGeeks: 8-Puzzle Problem](https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/)
3. [CS50 AI Notes](https://cs50.harvard.edu/ai/2024/notes/0/)

---

## Author

**Vishvendra Reddy Bhoomidi**  
Master's Student in Artificial Intelligence, University of Michigan-Dearborn
