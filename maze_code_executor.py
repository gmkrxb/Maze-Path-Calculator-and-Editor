import tkinter as tk

class MazeCodeExecutor(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.text_code = tk.Text(self, height=30)
        self.text_code.pack(fill=tk.BOTH, expand=True)

        self.btn_execute = tk.Button(self, text="执行代码", command=self.execute_code)
        self.btn_execute.pack(pady=10)

    def execute_code(self):
        code = self.text_code.get("1.0", tk.END)
        try:
            exec(code, {
                'creat': self.create_blank_maze,
                'random': self.create_random_maze,
                'set': self.set_maze_element,
                'maze': self.parent.maze,
                'start': self.parent.start,
                'end': self.parent.end,
                'update_maze': self.parent.update_maze,
                'update_status': self.parent.update_status
            })
            self.parent.update_status("代码执行成功")
        except Exception as e:
            self.parent.update_status(f"代码执行错误: {str(e)}")

    def create_blank_maze(self, width, height):
        self.parent.maze = np.zeros((height, width), dtype=int)
        self.parent.start = (0, 0)
        self.parent.end = (height - 1, width - 1)
        self.parent.update_maze()

    def create_random_maze(self, complexity):
        width, height = self.parent.maze.shape[1], self.parent.maze.shape[0]
        self.parent.maze = self.parent.solver.generate_maze_dfs(width, height)
        self.parent.start = (0, 0)
        self.parent.end = (height - 1, width - 1)
        self.parent.update_maze()

    def set_maze_element(self, element, x, y, *args):
        if element == 's':
            self.parent.start = (y, x)
        elif element == 'e':
            self.parent.end = (y, x)
        elif element == 'wall':
            if len(args) == 0:
                self.parent.maze[y, x] = 1
            elif len(args) == 1:
                if args[0] == 'x':
                    self.parent.maze[:, x] = 1
                elif args[0] == 'y':
                    self.parent.maze[y, :] = 1
            elif len(args) == 2:
                a, b = args
                if a == 'x':
                    for i in range(0, self.parent.maze.shape[0], int(b)):
                        self.parent.maze[i, x] = 1
                elif a == 'y':
                    for i in range(0, self.parent.maze.shape[1], int(b)):
                        self.parent.maze[y, i] = 1
        self.parent.update_maze()
