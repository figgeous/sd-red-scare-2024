import heapq
from collections import defaultdict

def dijkstra(graph, start, goal):
    # Priority queue to store (distance, node)
    pq = []
    # Distances dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Push the start node with distance 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the goal node, return the distance
        if current_node == goal:
            print(current_distance)
            return
        
        # If the current distance is greater than the recorded distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Iterate over neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path is found, update the distance and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # If the goal node is not reachable
    print(-1)
    return

# Example usage
if __name__ == "__main__":
    n, m, r = map(int, input().strip().split())
    start, end = input().split()
    V = []
    R = []

    for i in range(n):
        temp = input()
        if "*" in temp:
            R.append(temp.split(" ")[0])
            V.append(temp.split(" ")[0])
        else:
            V.append(temp)

    # Initialize the graph with all nodes
    graph = defaultdict(list)
    for node in V:
        graph[node] = []

    for i in range(m):
        u, direction, v = input().split()        
        if u in R or v in R:
            match direction:
                case "--":
                    graph[u].append((v, 1))
                    graph[v].append((u, 1))
                case "->":
                    graph[u].append((v, 1))
        else:
            match direction:
                case "--":
                    graph[u].append((v, 0))
                    graph[v].append((u, 0))
                case "->":
                    graph[u].append((v, 0))            

    dijkstra(graph, start, end)
