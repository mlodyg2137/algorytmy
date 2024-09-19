from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # liczba węzłów
        self.graph = defaultdict(dict)  # graf jako słownik sąsiedztwa

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity  # dodajemy krawędź z pojemnością

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for v, capacity in self.graph[u].items():
                if not visited[v] and capacity > 0:  # jeszcze nieodwiedzony i ma pojemność
                    parent[v] = u
                    if v == sink:
                        return True  # znaleźliśmy ścieżkę do ujścia
                    queue.append(v)
                    visited[v] = True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] = self.graph.get(v, {}).get(u, 0) + path_flow
                v = parent[v]

        return max_flow


# Przykład użycia
g = Graph(4)
g.add_edge(0, 1, 20)
g.add_edge(0, 2, 10)
g.add_edge(1, 3, 10)
g.add_edge(2, 3, 10)
print("Maksymalny przepływ:", g.ford_fulkerson(0, 3))
