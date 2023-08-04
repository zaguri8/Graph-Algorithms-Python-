import heapq
from Prims import  Graph,Edge
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, v):
        self.parent[v] = v
        self.rank[v] = 0

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                self.parent[xr] = yr
            else:
                self.parent[yr] = xr
                if self.rank[xr] == self.rank[yr]:
                    self.rank[xr] += 1



# algorithm Kruskal(G) is
#     F:= ∅
#     for each v ∈ G.V do
#         MAKE-SET(v)
#     for each (u, v) in G.E ordered by weight(u, v), increasing do
#         if FIND-SET(u) ≠ FIND-SET(v) then
#             F:= F ∪ {(u, v)} ∪ {(v, u)}
#             UNION(FIND-SET(u), FIND-SET(v))
#     return F


def Kruskal(G: Graph):
    F = set()
    U = UnionFind()
    Q = []
    for v in G.V:
        U.make_set(v)
        for e in G.E[v]:
            heapq.heappush(Q, (e.weight, e))

    while Q:
        w, e = heapq.heappop(Q)
        source = e.source
        sink = e.sink
        c1 = U.find(source)
        c2 = U.find(sink)
        if c1 != c2:
            F.add((source, e))
            U.union(c1, c2)
    return F


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


F = Kruskal(graph)


print("\033[31mKruskal\033[0m")
for vertex, edge in F:
    if edge is not None:
        print(f"Vertex: {vertex}, Connected by Edge: ({edge.source}, {edge.sink}, {edge.weight})")
    else:
        print(f"Vertex: {vertex}, Starting vertex")