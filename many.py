import dataclasses

from helpers.bellman_ford import bellman_ford
from helpers.helpers import preprocess_graph, build_adj_matrix

"""
Pseudo code:
    Read through the input vertices.
    Store all in a name to vertexID mapping.
    If vertex is red then store in red node set
    Create an adjacency matrix with the number of vertices.
    Iterate through the edges and add to the adjacency matrix.
    If direction is "-->" then:
        Add vertices to a vertex weight list. If edge ends in a red node then weight is 1 else 0.
        return bellman_ford to find the heaviest path from source to all nodes.
    else:
        not supported
    Run bellman_ford to find the heaviest path from source to target.
    Return the result.
"""
import sys

if __name__ == "__main__":
    n, m, n_of_r = map(int, sys.stdin.readline().strip().split())
    source_name, target_name = sys.stdin.readline().split()

    adj_matrix, red_nodes, is_directed, source, target = build_adj_matrix(n, m, source_name, target_name)

    mod_adj_matrix = preprocess_graph(adj_matrix, red_nodes, is_directed)

    result = bellman_ford(mod_adj_matrix, source, target)
    print(result)

    exit(0)



