import heapq
from collections import defaultdict
import os
import csv

def dijkstra(graph, start, goal, output_writer, file_name):
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
            output_writer.writerow([file_name, current_distance])
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
    output_writer.writerow([file_name, -1])
    return

# Example usage
def process_file(file_path, output_writer):
    with open(file_path, 'r') as file:
        n, m, r = map(int, file.readline().strip().split())
        start, end = file.readline().strip().split()

        V = []
        R = []

        for i in range(n):
            temp = file.readline().strip()
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
            u, direction, v = file.readline().split()        
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

    dijkstra(graph, start, end, output_writer, os.path.basename(file_path))


data_dir = "./data"
combined_output_path = "./results/few.csv"
os.makedirs(os.path.dirname(combined_output_path), exist_ok=True)  # Ensure output directory exists

# Open the CSV file and write the header
with open(combined_output_path, 'w', newline='') as combined_output:
    csv_writer = csv.writer(combined_output)
    csv_writer.writerow(["File Name", "F"])  # CSV header

    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_dir, filename)
            process_file(file_path, csv_writer)
