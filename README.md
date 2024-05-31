# Traveling Salesman Problem Solver

This Python script provides solutions to the Traveling Salesman Problem (TSP) using various search algorithms.

## Overview

The script offers three search algorithms to solve the TSP:
- A* Algorithm
- Depth-First Search (DFS)
- Uniform Cost Search (UCS)

It allows users to choose from pre-defined graphs or input their own adjacency matrix to solve the TSP for a given set of cities.

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the script by executing `python tsp_solver.py`.
4. Follow the on-screen menu prompts to select options:
    - **1**: Use the first pre-defined graph.
    - **2**: Use the second pre-defined graph.
    - **3**: Use a graph from the `test1.txt` file.
    - **4**: Use a graph from the `test2.txt` file.
    - **5**: Input your own adjacency matrix.
    - **0**: Exit the program.

## Graph Options

### Pre-defined Graphs
1. **Graph 1**: A 4-node graph with distances between nodes.
2. **Graph 2**: A 10-node graph with distances between nodes.

### External Files
1. **test1.txt**: Contains a custom graph.
2. **test2.txt**: Contains another custom graph.

## Results

The script will display the results of each algorithm along with the execution time for each.

- **A***: Result of the A* Algorithm.
- **DFS**: Result of Depth-First Search.
- **UCS**: Result of Uniform Cost Search.

## Note

- Ensure the input graph is in the correct format, either by following the provided examples or by using the custom input option carefully.
