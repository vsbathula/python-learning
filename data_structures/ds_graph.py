"""'
Graph
A graph is a collection of nodes (vertices) and edges connecting them.
Graphs can be either directed (edges have a direction) or undirected (edges have no direction).
They are often used to represent networks, such as social networks, maps, or computer networks.

Key Operations:
Add Vertex: Add a node to the graph.
Add Edge: Add an edge between two nodes.
Traverse: Visit all nodes (using BFS or DFS).
Search: Find a path between two nodes.
"""


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)  # For an undirected graph

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f'{vertex}: {edges}')


# Usage
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_edge("A", "B")
g.add_edge("A", "C")

g.print_graph()