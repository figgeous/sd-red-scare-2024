import os
from collections import deque, defaultdict

from helpers.constants import DATA_DIR


def parse_input(file_path):
    """Helper function for parsing an input file.
       First iterates through the nodes and adds them to a dictionary. Also adds red nodes to a set.
       Then iterates through the edges and adds them to a list. If it is an edge between two red nodes 
       or between two non-red, it is ignored.
       Also takes into account if the edge is directed or not.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    n, m, r = map(int, lines[0].split())

    s, t = lines[1].split()

    vertices = {}
    red_vertices = set()

    for i in range(2, n + 2):
        line = lines[i].strip()
        if line.endswith('*'):
            vertex = line.replace(' *', '')
            red_vertices.add(vertex)
            vertices[vertex] = []
        else:
            vertex = line.replace(' *', '')
            vertices[vertex] = []

    edges = []

    for i in range(n + 2, len(lines)):
        line = lines[i].strip()
        if '--' in line:
            u, v = map(str.strip, line.split('--'))
            if u in red_vertices and v in red_vertices:
                continue
            if u not in red_vertices and v not in red_vertices:
                continue
            vertices[u].append(v)
            vertices[v].append(u)
            edges.append((u, v))
        elif '->' in line:
            u, v = map(str.strip, line.split('->'))
            if u in red_vertices and v in red_vertices:
                continue
            if u not in red_vertices and v not in red_vertices:
                continue
            vertices[u].append(v)
            edges.append((u, v))

    return vertices, s, t, red_vertices, edges

def build_graph(vertices, edges):
    """Helper function for building a graph from the edges list. (obsolete with the current implementation)"""
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        if v in vertices and u in vertices[v]:
            graph[v].append(u)

    return graph

def bfs(graph, start, target):
    """Perform BFS to find if a path exists. Code adapted from this implementation: 
       https://www.datacamp.com/tutorial/breadth-first-search-in-python
       so that it is not a traversal, but stops when the target is found.
    """
    queue = deque()
    queue.append(start)
    visited = set()

    while queue:
        current = queue.popleft()

        if current == target:
            return True

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False

def process_files(folder_path):
    """Helper function to process all files that end in .txt aka are valid input in the data folder."""
    results = {}

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)

            vertices, s, t, _, edges = parse_input(file_path)

            result = bfs(vertices, s, t)
            results[file_name] = result

    return results

if __name__ == "__main__":
    # to replicate the results, replace the folder path with the path to the data folder on your computer
    results = process_files(DATA_DIR)
    results = dict(sorted(results.items()))

    for file_name, result in results.items():
        print(f"{file_name}: {'true' if result else 'false'}")
