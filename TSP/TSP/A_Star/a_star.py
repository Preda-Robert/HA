import heapq

class State:
    def __init__(self, current_city, visited, cost, path):
        self.current_city = current_city
        self.visited = visited
        self.cost = cost
        self.path = path

    def __lt__(self, other):
        return self.cost < other.cost

def tsp_a_star(graph, start):
    n = len(graph)
    pq = []
    # Create an initial state for the algorithm
    initial_state = State(start, set([start]), 0, [start])
    # Push the initial state onto the priority queue
    heapq.heappush(pq, (0, initial_state))

    while pq:
        _, current_state = heapq.heappop(pq)
        
        # If all cities have been visited, return to the starting city
        if len(current_state.visited) == n:
            return current_state.cost + graph[current_state.current_city][start], current_state.path + [start]

        for next_city in range(n):
            if next_city not in current_state.visited:
                # Create a new set of visited cities by copying the current set and adding the next city
                new_visited = current_state.visited.copy()
                new_visited.add(next_city)
                # Calculate the new cost of the path by adding the cost of moving to the next city
                new_cost = current_state.cost + graph[current_state.current_city][next_city]
                # Update the path with the next city
                new_path = current_state.path + [next_city]
                # Calculate the heuristic cost using the minimum spanning tree heuristic
                heuristic_cost = mst_heuristic(graph, new_visited, next_city, start)
                # Calculate the total cost by adding the new cost and the heuristic cost
                total_cost = new_cost + heuristic_cost
                # Create a new state with the next city, updated visited set, updated cost, and updated path
                new_state = State(next_city, new_visited, new_cost, new_path)
                # Push the new state onto the priority queue with its total cost
                heapq.heappush(pq, (total_cost, new_state))

def mst_heuristic(graph, visited, current_city, start):
    unvisited = set(range(len(graph))) - visited
    if not unvisited:
        return graph[current_city][start]
    mst_cost = 0
    unvisited = list(unvisited)
    if not unvisited:
        return graph[current_city][start]

    # Start Prim's algorithm from any unvisited city
    first_city = unvisited[0]
    mst_edges = [(0, first_city)]
    in_mst = set()
    edge_costs = {city: float('inf') for city in unvisited}

    while unvisited:
        cost, city = heapq.heappop(mst_edges)
        if city in in_mst:
            continue
        in_mst.add(city)
        mst_cost += cost
        unvisited.remove(city)
        
        for neighbor in unvisited:
            if graph[city][neighbor] < edge_costs[neighbor]:
                edge_costs[neighbor] = graph[city][neighbor]
                heapq.heappush(mst_edges, (graph[city][neighbor], neighbor))
    
    # Add the cost to return to the start city if there are still unvisited cities
    min_return_cost = min(graph[unvisited_city][start] for unvisited_city in unvisited) if unvisited else 0
    
    return mst_cost + min_return_cost
