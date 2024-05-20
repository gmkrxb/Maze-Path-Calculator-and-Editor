import numpy as np
from shortest_path_solver import ShortestPathSolver
from all_paths_solver import AllPathsSolver

class MazeSolver:
    def __init__(self):
        self.shortest_path_solver = ShortestPathSolver()
        self.all_paths_solver = AllPathsSolver()

    def generate_maze_dfs(self, width, height):
        maze = np.ones((height, width), dtype=int)
        stack = [(0, 0)]
        maze[0, 0] = 0

        def neighbors(x, y):
            steps = [(-2, 0), (2, 0), (0, -2), (0, 2)]
            return [(x + dx, y + dy) for dx, dy in steps if 0 <= x + dx < height and 0 <= y + dy < width]

        while stack:
            x, y = stack[-1]
            nbs = [(nx, ny) for nx, ny in neighbors(x, y) if maze[nx, ny] == 1]
            if nbs:
                nx, ny = nbs[np.random.randint(len(nbs))]
                maze[(x + nx) // 2, (y + ny) // 2] = 0
                maze[nx, ny] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

        return maze

    def find_shortest_path(self, maze, start, end):
        return self.shortest_path_solver.find_shortest_path(maze, start, end)

    def count_all_paths(self, maze, start, end):
        return self.all_paths_solver.count_all_paths(maze, start, end)
