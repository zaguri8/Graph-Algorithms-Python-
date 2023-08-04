

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
        self.E[u].append(e)



class TarjanSCC:
     def __init__(self, G : Graph) -> None:
          self.G = G


     def getSCC(self):
            index = {}
            lowlink = {}
            current_index = 0
            sc_components = []
            stack = []
            onStack = set()
            def scc(v):
                nonlocal current_index
                index[v] = lowlink[v] = current_index 
                current_index += 1
                onStack.add(v)
                stack.append(v)
                for e in self.G.E[v]:
                     w = e.sink

                     if w not in index:
                          scc(w)
                          lowlink[v] = min(lowlink[v], lowlink[w])
                     elif w in onStack:
                          lowlink[v] = min(lowlink[v], index[w])


                if lowlink[v] == index[v]:
                     component = []
                     
                     while len(stack) > 0:
                        w = stack.pop()
                        onStack.remove(w)
                        component.append(w)
                        if w == v:
                             break
                     sc_components.append(component)    
        
            for v in self.G.V:
                 if v not in index:
                      scc(v)
            
            return sc_components
     


graph = Graph()     

graph.add_vertex(1)
graph.add_vertex(2)

graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)


graph.addEdge(1,2,3)
graph.addEdge(2,3,1)
graph.addEdge(4,3,1)
graph.addEdge(4,5,2)
graph.addEdge(5,6,4)
graph.addEdge(6,2,2)
graph.addEdge(6,3,3)
graph.addEdge(3,2,2)
graph.addEdge(4,1,2)
graph.addEdge(3,1,1)


tarjan = TarjanSCC(graph)

SCC = tarjan.getSCC()

for component in SCC:
     print(component)