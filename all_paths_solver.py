class AllPathsSolver:
    def count_all_paths(self, maze, start, end, current=None, visited=None):
        if current is None:
            current = start
            visited = set()
        if current == end:
            return 1
        if current in visited or maze[current[0]][current[1]] == 1:
            return 0

        visited.add(current)
        paths = 0
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < maze.shape[0] and 0 <= neighbor[1] < maze.shape[1]:
                paths += self.count_all_paths(maze, start, end, neighbor, visited.copy())
        visited.remove(current)
        return paths
