from queue import Queue

class ShortestPathSolver:
    def find_shortest_path(self, maze, start, end):
        queue = Queue()
        queue.put((start, [start]))
        visited = set()
        visited.add(start)

        while not queue.empty():
            current, path = queue.get()
            if current == end:
                return path

            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if (0 <= neighbor[0] < maze.shape[0] and 0 <= neighbor[1] < maze.shape[1] and
                        maze[neighbor] == 0 and neighbor not in visited):
                    visited.add(neighbor)
                    queue.put((neighbor, path + [neighbor]))

        return None
