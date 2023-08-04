

import heapq

def dijsktra_matrix(matrix, start):
    dirs = [(1,0), (0, 1), (-1,0), (0,-1)]
    queue = [(matrix[start[1]][start[0]], start)]
    n = len(matrix)
    m = len(matrix[0])  
    dist_table = [[float('inf')] * m  for _ in range(n)]
    dist_table[start[1]][start[0]] = 0
    while queue:
        dist, (x, y) = heapq.heappop(queue)
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_dist = matrix[ny][nx] + dist
                if new_dist < dist_table[ny][nx]:
                    dist_table[ny][nx] = new_dist 
                    heapq.heappush(queue, (new_dist, (nx, ny)))

    return dist_table




matrix = [[1,2,3,4],
          [1,2,3,4],
          [1,2,3,4]]


shortest_paths = dijsktra_matrix(matrix, (0, 0))


print(shortest_paths)