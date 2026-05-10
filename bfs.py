# Python3 Program to print BFS traversal
from collections import defaultdict

# This class represents a graph using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print BFS traversal
    def BFS(self, s):

        visited = set()
        queue = []

        queue.append(s)
        visited.add(s)

        while queue:

            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

# Driver code
g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is BFS Traversal (starting from vertex 2)")
g.BFS(2)