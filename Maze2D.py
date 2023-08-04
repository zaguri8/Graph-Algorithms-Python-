import random

class Maze:
    def __init__(self, m, n) -> None:
        self.matrix = [['Not Empty' for _ in range(m)] for _ in range(n)]
        self.generate()

    def print(self):
        for row in self.matrix:
            for col in row:
                print('#' if col == 'Not Empty' else ' ',end='  ')
            print()
    

    def generate(self):
            w = len(self.matrix[0])
            h = len(self.matrix)

            start = (random.randint(0, w //2) * 2, random.randint(0, h//2) * 2)

            self.matrix[start[1]][start[0]] = 'Empty'
            frontier = [(start[1], start[0], dy, dx) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]

            while frontier:
                y, x, dy, dx = random.choice(frontier)
                ny = y + 2 * dy
                nx = x + 2 * dx
                if 0 <= ny < h and 0 <= nx < w and self.matrix[ny][nx] == 'Not Empty':
                    self.matrix[y + dy][x + dx] = 'Empty'
                    self.matrix[ny][nx] = 'Empty'
                    frontier.extend([(ny, nx, ddy, ddx) for ddx, ddy in [(0, 1), (1, 0), (0, -1), (-1, 0)]])
                else:
                    frontier.remove((y, x, dy, dx))
maze = Maze(21,21)


maze.print()