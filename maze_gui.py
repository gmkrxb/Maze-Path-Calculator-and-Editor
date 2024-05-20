import tkinter as tk
from tkinter import messagebox, filedialog
from maze_solver import MazeSolver
from maze_utilities import load_maze_from_csv, display_maze
from maze_editor import MazeEditor

class MazeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('迷宫路径计算器')
        self.geometry('800x600')
        self.solver = MazeSolver()
        self.maze = None
        self.start = None
        self.end = None
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="寻找最短路径", command=self.solve_shortest_path).pack(pady=10)
        tk.Button(self, text="寻找所有路径", command=self.count_all_paths).pack(pady=10)
        tk.Button(self, text="加载迷宫", command=self.load_maze).pack(pady=10)
        tk.Button(self, text="打开迷宫编辑器", command=self.open_maze_editor).pack(pady=10)
        self.canvas = tk.Canvas(self, width=600, height=400, bg="white")
        self.canvas.pack(pady=20)
        self.canvas.bind("<Configure>", self.resize_canvas)

    def resize_canvas(self, event):
        if self.maze is not None:
            display_maze(self.canvas, self.maze, self.start, self.end)

    def load_maze(self):
        self.maze, self.start, self.end = load_maze_from_csv()
        if self.maze is not None:
            display_maze(self.canvas, self.maze, self.start, self.end)

    def solve_shortest_path(self):
        if self.maze is not None:
            path = self.solver.find_shortest_path(self.maze, self.start, self.end)
            if path:
                display_maze(self.canvas, self.maze, self.start, self.end, path)
            else:
                messagebox.showinfo("结果", "没有找到路径")

    def count_all_paths(self):
        if self.maze is not None:
            num_paths = self.solver.count_all_paths(self.maze, self.start, self.end)
            messagebox.showinfo("路径总数", f"总路径数: {num_paths}")

    def open_maze_editor(self):
        editor = MazeEditor(self)
        editor.grab_set()

if __name__ == "__main__":
    app = MazeApp()
    app.mainloop()
