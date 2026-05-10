import sys

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def minDistance(self, dist, visited):

        minimum = sys.maxsize

        for v in range(self.V):
            if dist[v] < minimum and not visited[v]:
                minimum = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0

        visited = [False] * self.V

        for _ in range(self.V):

            u = self.minDistance(dist, visited)
            visited[u] = True

            for v in range(self.V):

                if (self.graph[u][v] > 0 and
                    not visited[v] and
                    dist[v] > dist[u] + self.graph[u][v]):

                    dist[v] = dist[u] + self.graph[u][v]

        print("Vertex \tDistance from Source")

        for i in range(self.V):
            print(i, "\t", dist[i])


# Driver Code
g = Graph(4)

g.graph = [
[0, 4, 1, 0],
[4, 0, 2, 1],
[1, 2, 0, 5],
[0, 1, 5, 0]
]

g.dijkstra(0)
