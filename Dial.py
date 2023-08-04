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




def dials(G: Graph, start, weight):
     
     buckets = [[] for _ in range(weight * len(G.V) + 1)]

     buckets[0].append(start)
     i = 0
     dist = {v :  float('inf') for v in G.V}
     dist[start] = 0
     while i < len(buckets):
          while buckets[i]:
               u = buckets[i].pop()
               for e in G.E[u]:
                    w = e.sink
                    new_dist = dist[u] + e.weight
                    if new_dist < dist[w]:
                         if dist[w] != float('inf'):
                             buckets[dist[w]].remove(w)
                         dist[w] = new_dist
                         buckets[new_dist].append(w)
          i += 1                   
     return dist


graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)

# 2 + 1 + 1
graph.addEdge(1, 3, 2)
graph.addEdge(3, 5, 1)
graph.addEdge(5, 1, 1)
graph.addEdge(5, 4, 2)
graph.addEdge(2, 4, 1)
graph.addEdge(4, 5 ,2)
graph.addEdge(5, 2 ,1)


dials_out = dials(graph, 1 , 2)

print(dials_out)