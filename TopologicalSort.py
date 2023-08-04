

from collections import deque


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



def topological_sort(G : Graph):

     indegree_map = {node: 0 for node in graph.V}
     for node in graph.V:
        for neighbor in graph.E[node]:
            indegree_map[neighbor.sink] += 1
    # Queue of all nodes with no incoming edge
     zero_indegree_queue = deque([node for node in indegree_map if indegree_map[node] == 0])
     topological_order = []
     while zero_indegree_queue:
          v = zero_indegree_queue.popleft()
          topological_order.append(v)
          for e in G.E[v]:
              w = e.sink
              indegree_map[w] -= 1 
              if indegree_map[w] == 0:
                   zero_indegree_queue.append(w)
     if len(topological_order) ==  len(G.V):
        return topological_order
     else:
        raise ValueError("[topological sort error] G Contains Cycles")
     

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)


graph.addEdge(1, 3, 2)
graph.addEdge(3, 4, 2)
graph.addEdge(4, 5 ,3)
graph.addEdge(5, 2 ,2)     


sorted = topological_sort(graph)

print(sorted)