

import heapq


class Graph: 
    def __init__(self,n,m) -> None:
        self.m = m
        self.n = n
        self.matrix = [[1 for _ in range(m)] for _ in range(n)]

    def add_edge(self,u,v):
        self.matrix[u][v] = 1    


    def heuristic(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p2[1] -p2[1]) # Manhattan distance
    
    def aStar(self, start, end):
        queue = [(float('inf'), start)]

        visited = set()
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        solution = []
        cost_map = {}
        while queue:
            _,v = heapq.heappop(queue)

            solution.append(v)

            if v == end:
                return solution
            
            visited.add(v)
            
            for (dx, dy) in dirs:
                ny = dy + v[0]
                nx = dx + v[1]

                if 0 <= nx < self.m and 0 <= ny < self.n and (nx, ny) not in visited:
                    cost = self.heuristic((nx, ny), end)
                    cost_map[(nx, ny)] = cost
                    heapq.heappush(queue, (cost, (nx, ny)))
        return solution
    


graph = Graph(5, 5)

graph.add_edge(1, 4)

sol = graph.aStar((0,0), (4, 4))

m = graph.matrix

for (x, y) in sol:
    m[y][x] = 0

for row in m:
    print(row)