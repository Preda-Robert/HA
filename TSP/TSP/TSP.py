import sys
from DFS.dfs_tsp import dfs_tsp
from Uniform.ucs import ucs_tsp
from A_Star.a_star import tsp_a_star
from InputReader import read_graph_from_file, input_graph
import time

def print_menu():
    print("Choose an option:")
    print("1: Use first pre-defined graph")
    print("2: Use second pre-defined graph")
    print("3: Use graph from gr24 file")
    print("4: Use graph from gr17 file")
    print("5: Input your own adjacency matrix")
    print("0: Exit")

def main():
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            graph = [
    [0, 1, 5, 2],
    [1, 0, 3, 2],
    [5, 3, 0, 4],
    [2, 2, 4, 0]
]
        elif choice == 2:
            graph = [
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
]
        elif choice == 3:
            graph = read_graph_from_file("test1.txt")
        elif choice == 4:
            graph = read_graph_from_file("test2.txt")
        elif choice == 5:
            graph = input_graph()
        else:
            print("Invalid choice. Please try again.")
            continue

        start = 0
        print("Results for the chosen graph:")
        start_time = time.time()
        result = tsp_a_star(graph, start)
        end_time = time.time()
        print("A*:", result)
        print("Execution Time for A*:", end_time - start_time, "seconds")

        start_time = time.time()
        result = dfs_tsp(graph, start)
        end_time = time.time()
        print("DFS:", result)
        print("Execution Time for DFS:", end_time - start_time, "seconds")

        start_time = time.time()
        result = ucs_tsp(graph, start)
        end_time = time.time()
        print("UCS:", result)
        print("Execution Time for UCS:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
