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