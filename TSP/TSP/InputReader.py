def read_graph_from_file(filename):
    graph = []
    i = 0
    j = 0
    with open(filename) as file:
        n = int(file.readline())
        for k in range(n):
            graph.append([0] * n)
        for line in file:
            for cost in line.split():
                if(cost == '0'):
                    graph[i][i] = 0
                    i = i + 1
                    j = 0
                else:
                    graph[i][j] = int(cost)
                    graph[j][i] = int(cost)
                    j = j + 1

    return graph

def input_graph():
    n = int(input("Enter the number of nodes: "))
    graph = []
    print("Enter the adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Invalid input. Each row must have exactly {} values.".format(n))
            sys.exit(1)
        graph.append(row)
    return graph