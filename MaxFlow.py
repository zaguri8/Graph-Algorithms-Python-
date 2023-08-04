from collections import deque
import heapq
class Edge:
    def __init__(self, source, sink, capacity):
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.reverse_edge = None

class MaxFlow:
    def __init__(self):
        self.flow = {}
        self.adj = {}

    def add_vertex(self, v):
        self.adj[v] = []

    def add_edge(self, u, v, c):
        edge = Edge(u, v, c)
        reverse_edge = Edge(v, u, 0)
        edge.reverse_edge = reverse_edge
        reverse_edge.reverse_edge = edge
        self.adj[u].append(edge)
        self.adj[v].append(reverse_edge)
        self.flow[edge] = 0
        self.flow[reverse_edge] = 0

    def find_path(self, source, sink):
        paths = {source: []}
        queue = deque()
        queue.append(source)
        while queue:
            vertex = queue.popleft()
            for e in self.adj[vertex]:
                rgc = e.capacity - self.flow[e] # residual graph capacity
                if rgc > 0 and e.sink not in paths:
                    paths[e.sink] = paths[vertex] + [(e, rgc)]
                    if e.sink == sink:
                        return paths[sink]
                    queue.append(e.sink)

    def max_flow(self, source, sink):
        path = self.find_path(source, sink)
        while path is not None:
            bottleneck = min(rgc for e, rgc in path)
            for e, _ in path:
                self.flow[e] += bottleneck
                self.flow[e.reverse_edge] -= bottleneck
            path = self.find_path(source, sink)
        return sum(self.flow[e] for e in self.adj[source] if isinstance(e, Edge))

graph = MaxFlow()

men = ['m1', 'm2', 'm3']
women = ['w1', 'w2', 'w3']
matchers = ["matcher_1", "matcher_2"]

matchers_men = {
    "matcher_1": ["m1", "m3"],
    "matcher_2": ["m2"],
}

matchers_women = {
    "matcher_1": ["w1", "w2"],
    "matcher_2": ["w3"],
}

matchers_capacity = {
    "matcher_1": 2,
    "matcher_2": 2,
}
source = "source"
sink = "sink"

graph.add_vertex(source)
graph.add_vertex(sink)

for man in men:
    graph.add_vertex(man)
    graph.add_edge(source, man, 1)

for woman in women:
    graph.add_vertex(woman)
    graph.add_edge(woman, sink, 1)

for matcher in matchers:
    smi = matcher + "_source"
    fmi = matcher + "_sink"

    graph.add_vertex(smi)
    graph.add_vertex(fmi)

    graph.add_edge(smi, fmi, matchers_capacity[matcher])  # edge between SMi and FMi

    if matcher in matchers_men:
        for man in matchers_men[matcher]:
            graph.add_edge(man, smi, 1)  # edge from man to SMi

    if matcher in matchers_women:
        for woman in matchers_women[matcher]:
            graph.add_edge(fmi, woman, 1)  # edge from FMi to woman

max_flow = graph.max_flow(source, sink)

print(max_flow)







class UndirectedGraph:
    def __init__(self):
        self.adj = {}
        self.vertices = []

    def add_vertex(self, v):
        self.vertices.append(v)
        self.adj[v] = []
    def add_edge(self, v,u,weight):
        e = Edge(v,u,weight)
        e_rev = Edge(u,v,weight)
        self.adj[v].append(e)
        self.adj[u].append(e_rev)

    def dijkstra(self, source):
        import heapq

        queue = []
        heapq.heappush(queue, (0, source))  # Heap is initialized with a tuple (priority, task)
        dist = {}
        parent = {}
        for v in self.adj.keys():
            dist[v] = float('inf')
        dist[source] = 0

        while queue:
            (dist_vertex, vertex) = heapq.heappop(queue)  # Vertex with smallest distance will be popped first

            if dist_vertex != dist[vertex]:  # If this vertex's shortest path has been updated since being added to queue, skip
                continue

            for e in self.adj[vertex]:
                neighbor = e.sink
                neighbor_weight = e.capacity

                if dist[vertex] + neighbor_weight < dist[neighbor]:
                    dist[neighbor] = dist[vertex] + neighbor_weight
                    parent[neighbor] = vertex
                    heapq.heappush(queue, (dist[neighbor], neighbor))  # Add to queue with new distance as priority

        return parent, dist


def get_path(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

graph = UndirectedGraph()


matrix = [
    [  1,2,20,1  ],
    [  1,4,3,5  ],
    [  1,1,1,1  ],
    [  1,2,4,3  ]
]




def dijkstra_matrix(grid, source):
    n = len(grid)
    m = len(grid[0])
    dist = [[float('inf')]*n for _ in range(m)]
    queue = []
    parent = {}
    dist[source[0]][source[1]] = grid[source[0]][source[1]] 

    heapq.heappush(queue, (grid[source[0]][source[1]] ,source))

    dirs = [(0,1), (0,-1), (1,0), (-1,0)]

    while queue:
        curr_dist , (x, y) = heapq.heappop(queue)

        for dx,dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_dist = curr_dist + grid[nx][ny]   
                if new_dist < dist[nx][ny]:     
                    dist[nx][ny] = new_dist
                    parent[(nx,ny)] = (x, y)
                    heapq.heappush(queue, (new_dist, (nx, ny)))

    return dist,parent
               



dist, parent = dijkstra_matrix(matrix,(0,0))



def get_pathX(parent,source,sink):
    path = [sink]
    while path[-1] != source:
        path.append(parent[path[-1]])
    path.reverse()
    return path    

print(get_pathX(parent, (0,0), (len(matrix)-1, len(matrix[0]) - 1)))
