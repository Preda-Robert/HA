## Overview

The script offers three search algorithms to solve the TSP:
- A* Algorithm
- Depth-First Search (DFS)
- Uniform Cost Search (UCS)

It allows users to choose from pre-defined graphs or input their own adjacency matrix to solve the TSP for a given set of cities.

## How to Use

1. Run the script by executing `TSP.py`.
2. Follow the on-screen menu prompts to select options:
    - **1**: Use the first pre-defined graph.
    - **2**: Use the second pre-defined graph.
    - **3**: Use a graph from the `test1.txt` file, which contains data from gr24.tsp.
    - **4**: Use a graph from the `test2.txt` file, which contains data from gr17.tsp.
    - **5**: Input your own adjacency matrix.
    - **0**: Exit the program.


## Graph Options
Link for the gr datasets:
http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/
### Pre-defined Graphs
1. **Graph 1**: A 4-node graph with distances between nodes. It is represented by the following adjacency matrix:
    ```
    [0, 1, 5, 2],
    [1, 0, 3, 2],
    [5, 3, 0, 4],
    [2, 2, 4, 0]
    ```
2. **Graph 2**: A 10-node graph with distances between nodes. It is represented by the following adjacency matrix:
    ```
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    [10, 0, 10, 15, 20, 25, 30, 35, 40, 45],
    [15, 10, 0, 10, 15, 20, 25, 30, 35, 40],
    [20, 15, 10, 0, 10, 15, 20, 25, 30, 35],
    [25, 20, 15, 10, 0, 10, 15, 20, 25, 30],
    [30, 25, 20, 15, 10, 0, 10, 15, 20, 25],
    [35, 30, 25, 20, 15, 10, 0, 10, 15, 20],
    [40, 35, 30, 25, 20, 15, 10, 0, 10, 15],
    [45, 40, 35, 30, 25, 20, 15, 10, 0, 10],
    [50, 45, 40, 35, 30, 25, 20, 15, 10, 0]
    ```
### External Files
1. **test1.txt**: Contains the gr24 graph.
2. **test2.txt**: Contains the gr17 graph.

## Results

The script will display the results of each algorithm along with the execution time for each.

- **A***: Result of the A* Algorithm.
- **DFS**: Result of Depth-First Search.
- **UCS**: Result of Uniform Cost Search.
