# Associate with each vertex v of the graph a number C[v] 
# (the cheapest cost of a connection to v) and an edge E[v] (the edge providing that cheapest connection). To initialize these values, set all values of C[v] to +∞ (or to any number larger than the maximum edge weight) and set each E[v] to a special flag value indicating that there is no edge connecting v to earlier vertices.
# Initialize an empty forest F and a set Q of vertices that have not yet been included in F (initially, all vertices).
# Repeat the following steps until Q is empty:
# Find and remove a vertex v from Q having the minimum possible value of C[v]
# Add v to F
# Loop over the edges vw connecting v to other vertices w. For each such edge, 
# if w still belongs to Q and vw has smaller weight than C[w], perform the following steps:
# Set C[w] to the cost of edge vw
# Set E[w] to point to edge vw.
# Return F, which specifically includes the corresponding edges in E

import heapq

class Edge: 
    def __init__(self, source, sink, weight) -> None:
        self.source = source
        self.sink = sink
        self.weight = weight

    def __lt__(self, other):
            return self.weight < other.weight
class Graph:
    def __init__(self) -> None:
        self.E = {}
        self.V = []

    def add_vertex(self, v):
        self.E[v] = []
        self.V.append(v)

    def addEdge(self, u, v, w):
        e = Edge(u,v,w)
        e_rev = Edge(v,u,w)
        self.E[u].append(e)
        self.E[v].append(e_rev)



def prims(G: Graph, starting_vertex):
    C =  { v: float('inf') for v in G.V }
    E =  { v: None for v in G.V }
    Q = [(float('inf'), starting_vertex)]
    F = set()
    while Q:
        _,v = heapq.heappop(Q)
        if v not in F:
            F.add(v)
            for e in G.E[v]:
                w = e.sink
                if w not in F and e.weight < C[w]:
                    C[w] = e.weight
                    E[w] = e
                    heapq.heappush(Q, (C[w], w))
    return E
graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)


graph.addEdge(1, 3, 2)
graph.addEdge(3, 5, 1)
graph.addEdge(5, 1, 1)
graph.addEdge(5, 4, 13)
graph.addEdge(2, 4, 4)
graph.addEdge(4, 5 ,3)
graph.addEdge(5, 2 ,2)



print("\033[33mPrims\033[0m")
E  = prims(graph, 2)

for vertex, edge in E.items():
    if edge is not None:
        print(f"Vertex: {vertex}, Connected by Edge: ({edge.source}, {edge.sink}, {edge.weight})")