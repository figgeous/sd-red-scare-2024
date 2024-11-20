# Dijkstra adjusted implementation from:
# https://gist.github.com/kachayev/5990802
# file handling stackoverflow/Generative AI
# some comments AI generated

from collections import defaultdict
from heapq import *
import sys


def read_file_from_stdin():
    """
    Reads the content of the file piped into stdin.

    Returns:
    - str: Content of the piped file.
    """
    return sys.stdin.read()


def input_handling_for_few(file_content):
    lines = file_content.splitlines()

    n, m, r = map(int, lines[0].strip().split())

    n_lines_start_at = 2
    m_lines_start_at = n_lines_start_at + n

    start, terminal = lines[1].split()

    # handling of no existing edges
    if (m == 0):
        empty = {}
        return empty, start, terminal, 0

    # initiate Vertices and RedVertices sets
    V = set()
    R = set()

    # Vertices processing
    for i in range(n_lines_start_at, n_lines_start_at + n):
        temp = lines[i]
        if "*" in temp:
            R.add(temp.split()[0])
        else:
            V.add(temp)

    if start in R:
        start_node_cost = 1
    else:
        start_node_cost = 0

    adjacency_list_vertices = {}

    # Edges processing
    for i in range(m_lines_start_at, m_lines_start_at + m):
        u, direction, v = lines[i].split()

        if u not in adjacency_list_vertices:
            adjacency_list_vertices[u] = []
        adjacency_list_vertices[u].append((u, direction, v))

        adjacency_directed = {}
    for u, neighbors in adjacency_list_vertices.items():
        for neighbor in neighbors:
            u, direction, v = neighbor
            is_directed = (direction == '->')

            # Create forward edge
            if u not in adjacency_directed:
                adjacency_directed[u] = []
            weight = 1 if v in R else 0
            adjacency_directed[u].append((u, v, weight))

            # Create reverse edge if undirected
            if not is_directed:
                if v not in adjacency_directed:
                    adjacency_directed[v] = []
                weight = 1 if u in R else 0
                adjacency_directed[v].append((v, u, weight))

    return adjacency_directed, start, terminal, start_node_cost


def dijkstra(edges, start_node, terminal_node, start_node_cost_passed):
    if not edges:
        return -1

    # Initialize the priority queue, visited set, and distance tracker
    q = [(start_node_cost_passed, start_node,
          ())]  # Priority queue initialized with the start node
    seen_set = set()
    minimal_cost_set = {
        start_node: start_node_cost_passed}  # Tracks minimal cost to each node

    # Process nodes in priority queue
    while q:
        cost, current_node, path = heappop(q)  # Pop the lowest-cost node from the queue

        # If the node is not visited, process it
        if current_node not in seen_set:
            seen_set.add(current_node)
            path = (current_node, path)

            # If the target node is reached, return the result
            if current_node == terminal_node:
                return cost  # , path #If needed path

            # Explore neighbors of the current node
            for _, neighbor, edge_cost in edges.get(current_node,
                                                    []):  # Access neighbors directly
                if neighbor in seen_set:
                    continue

                # Calculate the total cost to reach the neighbor
                previous_cost = minimal_cost_set.get(neighbor, None)
                new_cost = cost + edge_cost

                if previous_cost is None or new_cost < previous_cost:
                    minimal_cost_set[neighbor] = new_cost
                    heappush(q, (new_cost, neighbor, path))

    return -1  # Return -1 if no path is found


def main():
    try:
        file_content = read_file_from_stdin()
        adjacency_directed, start_node, terminal_node, start_node_cost = input_handling_for_few(
            file_content)
        result = dijkstra(adjacency_directed, start_node, terminal_node,
                          start_node_cost)


        print(result)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
