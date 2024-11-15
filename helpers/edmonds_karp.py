import sys
from collections import deque

class EdmondsKarp:
    def __init__(self, residual_graph):
        self.residual_graph = residual_graph
        self.n = len(residual_graph)

    def _bfs(self, source, sink, parent):
        visited = [False] * self.n
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in range(self.n):
                capacity = self.residual_graph[u][v]
                if not visited[v] and capacity > 0:
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
                    visited[v] = True

        return False

    def _update_residual_graph(self, parent, sink, flow):
        v = sink
        while v != -1:
            u = parent[v]
            if u != -1:
                self.residual_graph[u][v] -= flow
                self.residual_graph[v][u] += flow
            v = u

    def run(self, source, sink):
        max_flow = 0
        parent = [-1] * self.n

        while self._bfs(source, sink, parent):
            path_flow = float('Inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.residual_graph[u][v])
                v = u

            self._update_residual_graph(parent, sink, path_flow)

            max_flow += path_flow
        return max_flow, self.residual_graph


if __name__ == '__main__':
    n, m = list(map(int, sys.stdin.readline().split()))

    n_plus = n + n + 2
    x_offset = 2
    y_offset = x_offset + n

    adj_matrix = [[0] * n_plus for _ in range(n_plus)]
    adj_matrix[0] = [0, 0] + [1] * n + [0] * n  # source
    for i in range(y_offset, len(adj_matrix)):
        adj_matrix[i][1] = 1

    for _ in range(m):
        p1, p2 = list(map(int, sys.stdin.readline().split()))
        adj_matrix[x_offset + p1 - 1][y_offset + p2 - 1] = 1
        adj_matrix[x_offset + p2 - 1][y_offset + p1 - 1] = 1

    edmonds_karp = EdmondsKarp(adj_matrix)
    max_flow, res_graph = edmonds_karp.run(0, 1)

    if max_flow == n:
        for i, node in enumerate(res_graph[y_offset:]):
            print(node[x_offset:y_offset].index(1) + 1)
    else:
        print("Impossible")