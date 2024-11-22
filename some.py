import copy
import sys

from helpers.bellman_ford import bellman_ford
from helpers.edmonds_karp import EdmondsKarp
from helpers.helpers import preprocess_graph, build_adj_matrix

"""
Pseudo code:
    Read through the input vertices.
    Store all in a name to vertexID mapping.
    If vertex is red then store in red list.
    Create an adjacency matrix with the number of vertices.
    Iterate through the edges and add to the adjacency matrix.
    If "--" then both directions are added.
    Connect s and t to super sink with edge weights of 1
    while red vertex list is not empty:
        Pop red vertex from the list and connect to super source with edge weight of 2
        Run Edmonds Karp to find the max flow between super source and super sink.
        If max_flow = 2 then return true
    return false
"""


if __name__ == "__main__":

    n, m, n_of_r = map(int, sys.stdin.readline().strip().split())
    source_name, target_name = sys.stdin.readline().split()
    adj_matrix = [[0] * (n + 2) for _ in range(n + 2)]
    adj_matrix, red_nodes, is_directed, source, target = build_adj_matrix(n, m, source_name, target_name)

    if is_directed:
        # If Many algorithm returns greater than zero then return True
        mod_adj_matrix = preprocess_graph(adj_matrix, red_nodes, is_directed)

        result = bellman_ford(mod_adj_matrix, source, target)
        print("True" if result < 0 else "False")
        exit(0)

    # Make space for super source and super sink. Add two cells.
    for i in range(n):
        adj_matrix[i] += [0, 0]
    adj_matrix.append([0] * (n + 2))
    adj_matrix.append([0] * (n + 2))

    super_source, super_sink = n, n + 1
    adj_matrix[source][super_sink] = 1
    adj_matrix[target][super_sink] = 1
    while red_nodes:
        red_node = red_nodes.pop()
        adj_matrix_copy = copy.deepcopy(adj_matrix)  # Make a deep copy
        adj_matrix_copy[super_source][red_node] = 2
        try:
            edmonds_karp = EdmondsKarp(adj_matrix_copy)
            max_flow, _ = edmonds_karp.run(super_source, super_sink)
        except RecursionError:
            print("RecursionError")
            exit(0)
        if max_flow == 2:
            print("True")
            exit(0)
    print("False")



