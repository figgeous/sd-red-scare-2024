import os
import csv
from collections import deque, defaultdict

def BFS_SP(graph, start, goal, output_writer, file_name):
    explored = []
    queue = [[start]]
    
    if start == goal:
        output_writer.writerow([file_name, "Same Node"])
        return
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    output_writer.writerow([file_name, len(new_path) - 1])
                    return
            explored.append(node)
    
    output_writer.writerow([file_name, -1])
    return

# Function to process a single file and write to output CSV
def process_file(file_path, output_writer):
    with open(file_path, 'r') as file:
        n, m, r = map(int, file.readline().strip().split())
        start, end = file.readline().strip().split()
        
        V = []
        R = []
        
        for _ in range(n):
            temp = file.readline().strip()
            if ("*" in temp and (temp.split(" ")[0]!= end and temp.split(" ")[0]!= start)):
                R.append(temp.split(" ")[0])
            else:
                V.append(temp)
        
        graph = defaultdict(list)
        
        for _ in range(m):
            u, direction, v = file.readline().strip().split()
            if u in R or v in R:
                continue
            
            match direction:
                case "--":
                    graph[u].append(v)
                    graph[v].append(u)
                case "->":
                    graph[u].append(v)
                #case "<-":
                #    graph[v].append(u)
        
        # Run BFS on the parsed graph and write output
        BFS_SP(graph, start, end, output_writer, os.path.basename(file_path))

# Directory containing input files


data_dir = "./data"
combined_output_path = "./results/none.csv"
os.makedirs(os.path.dirname(combined_output_path), exist_ok=True)  # Ensure output directory exists

# Open the CSV file and write header
with open(combined_output_path, 'w', newline='') as combined_output:
    csv_writer = csv.writer(combined_output)
    csv_writer.writerow(["File Name", "N"])  # CSV header

    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_dir, filename)
            process_file(file_path, csv_writer)
