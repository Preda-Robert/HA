def dfs_tsp(graph, start):
    n = len(graph)
    min_cost = float('inf')  
    best_path = []

    def dfs(city, visited, current_path, current_cost):
        nonlocal min_cost, best_path
        
        # If all cities have been visited
        if len(visited) == n:
            # Calculate the cost of returning to the starting city
            return_cost = current_cost + graph[current_path[-1]][start]
            # Update the minimum cost and best path if the return cost is less than the current minimum cost
            if return_cost < min_cost:
                min_cost = return_cost
                best_path = current_path + [start]
            return
        
        for next_city in range(n):
            if next_city not in visited:
                # Recursively call DFS with the next city, updated visited set, current path, and current cost
                dfs(next_city, visited | {next_city}, current_path + [next_city], current_cost + graph[city][next_city])

    # Start DFS from the starting city, with the starting city as visited, starting path, and cost 0
    dfs(start, {start}, [start], 0)
    return best_path, min_cost
