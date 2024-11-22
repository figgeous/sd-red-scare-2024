def bellman_ford(adj_matrix, source, target):
    """
    Bellman-Ford to find the shortest path cost (maximum red nodes) from source to target.

    Parameters:
    - adj_matrix: 2D list with weights.
    - source: Starting node.
    - target: Target node.

    Returns:
    - max_red_count: Maximum red nodes encountered on any path from source to target.
    """
    num_nodes = len(adj_matrix)
    distances = [float('inf')] * num_nodes
    distances[source] = 0

    # Relax all edges |V|-1 times
    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v in range(num_nodes):
                if adj_matrix[u][v] != float('inf'):
                    # Relaxation step
                    if distances[u] + adj_matrix[u][v] < distances[v]:
                        distances[v] = distances[u] + adj_matrix[u][v]

    # Check for negative-weight cycles
    for u in range(num_nodes):
        for v in range(num_nodes):
            if adj_matrix[u][v] != float('inf') and distances[u] + \
                    adj_matrix[u][v] < distances[v]:
                return "NegativeWeightCycle"

    return distances[target] if distances[target] != float('inf') else -1