import sys

from helpers.helpers import build_adj_matrix

"""
Pseudo code:
    Read through the input vertices.
    Store all in a name to vertexID mapping.
    If vertex is red then store in red list.
    Create an adjacency matrix with the number of vertices.
    Iterate through the edges and add to the adjacency matrix.
    If "--" then both directions are added.
    ???
"""


if __name__ == "__main__":

    n, m, n_of_r = map(int, sys.stdin.readline().strip().split())
    source_name, target_name = sys.stdin.readline().split()
    adj_matrix, red_nodes, is_directed, source, target = build_adj_matrix(n, m, source_name, target_name)




