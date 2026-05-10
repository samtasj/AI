# Python3 program to print DFS traversal
from collections import defaultdict

# This class represents a graph using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function used by DFS
    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # DFS Traversal
    def DFS(self, v):

        visited = set()
        self.DFSUtil(v, visited)

# Driver code
g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS Traversal (starting from vertex 2)")
g.DFS(2)