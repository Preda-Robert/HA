from heapq import heappop, heappush

def ucs_tsp(graph, start):
    n = len(graph)
    pq = [(0, start, [start])]
    min_cost = float('inf')
    best_path = []

    while pq:
        # Pop the state with the lowest cost from the priority queue
        cost, city, path = heappop(pq)
        
        if len(path) == n:
            # Calculate the cost of returning to the starting city
            return_cost = cost + graph[city][start]
            # Update the minimum cost and best path if the return cost is less than the current minimum cost
            if return_cost < min_cost:
                min_cost = return_cost
                best_path = path + [start]
            continue
        
        for next_city in range(n):
            if next_city not in path:
                # Push the new state onto the priority queue with the updated cost, next city, and updated path
                heappush(pq, (cost + graph[city][next_city], next_city, path + [next_city]))
    
    return best_path, min_cost