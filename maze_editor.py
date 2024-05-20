import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import numpy as np
from maze_utilities import save_maze_to_csv, load_maze_from_csv, display_maze
from maze_solver import MazeSolver
from maze_code_executor import MazeCodeExecutor

class MazeEditor(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('迷宫编辑器')
        self.geometry('1200x800')
        self.maze = None
        self.start = None
        self.end = None
        self.cell_size = 20
        self.is_drawing = False
        self.is_erasing = False
        self.solver = MazeSolver()
        self.create_widgets()

    def create_widgets(self):
        # 顶部按钮面板
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_new_maze = tk.Button(self.top_frame, text="新建迷宫", command=self.new_maze_dialog)
        self.btn_new_maze.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_save_maze = tk.Button(self.top_frame, text="保存迷宫", command=self.save_maze)
        self.btn_save_maze.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_load_maze = tk.Button(self.top_frame, text="加载迷宫", command=self.load_maze)
        self.btn_load_maze.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_pencil = tk.Button(self.top_frame, text="画笔", command=self.select_pencil)
        self.btn_pencil.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_eraser = tk.Button(self.top_frame, text="橡皮", command=self.select_eraser)
        self.btn_eraser.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_set_start = tk.Button(self.top_frame, text="设置起点", command=self.set_start)
        self.btn_set_start.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_set_end = tk.Button(self.top_frame, text="设置终点", command=self.set_end)
        self.btn_set_end.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_check_maze = tk.Button(self.top_frame, text="检查迷宫通畅性", command=self.check_maze)
        self.btn_check_maze.pack(side=tk.LEFT, padx=5, pady=5)

        # 迷宫和代码执行器区域
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # 左侧画布和控制面板
        self.left_frame = tk.Frame(self.main_frame, width=900, height=600)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.left_frame, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<B1-Motion>", self.draw_or_erase)
        self.canvas.bind("<Button-1>", self.draw_or_erase)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing_or_erasing)
        self.canvas.bind("<Configure>", self.resize_canvas)

        # 右侧代码执行器
        self.right_frame = tk.Frame(self.main_frame, width=300, height=600)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.code_executor = MazeCodeExecutor(self.right_frame)
        self.code_executor.pack(fill=tk.BOTH, expand=True)

        # 底部状态窗口
        self.status_frame = tk.Frame(self, height=100)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_text = tk.Text(self.status_frame, height=5, bg='lightgrey')
        self.status_text.pack(fill=tk.BOTH, expand=True)

    def resize_canvas(self, event):
        if self.maze is not None:
            display_maze(self.canvas, self.maze, self.start, self.end)

    def select_pencil(self):
        self.is_drawing = True
        self.is_erasing = False

    def select_eraser(self):
        self.is_drawing = False
        self.is_erasing = True

    def set_start(self):
        self.canvas.bind("<Button-1>", self.set_start_point)

    def set_end(self):
        self.canvas.bind("<Button-1>", self.set_end_point)

    def set_start_point(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        if self.maze[y, x] != 1:  # 不能在墙上设置起点
            self.start = (y, x)
            self.update_maze()
            self.canvas.unbind("<Button-1>")

    def set_end_point(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        if self.maze[y, x] != 1:  # 不能在墙上设置终点
            self.end = (y, x)
            self.update_maze()
            self.canvas.unbind("<Button-1>")

    def check_maze(self):
        if self.maze is not None:
            path = self.solver.find_shortest_path(self.maze, self.start, self.end)
            if path:
                messagebox.showinfo("检查结果", "迷宫通畅")
            else:
                messagebox.showinfo("检查结果", "迷宫不通畅")

    def draw_or_erase(self, event):
        if self.maze is not None:
            x, y = event.x // self.cell_size, event.y // self.cell_size
            if (x, y) != self.start and (x, y) != self.end:  # 不能在起点和终点上绘画
                if self.is_drawing:
                    self.maze[y, x] = 1
                elif self.is_erasing:
                    self.maze[y, x] = 0
            self.update_maze()

    def stop_drawing_or_erasing(self, event):
        self.is_drawing = False
        self.is_erasing = False

    def new_maze_dialog(self):
        dialog = NewMazeDialog(self)
        dialog.grab_set()
        dialog.focus_set()
        self.wait_window(dialog)
        if dialog.maze is not None:
            self.maze, self.start, self.end = dialog.maze, dialog.start, dialog.end
            self.update_maze()

    def save_maze(self):
        if self.maze is not None:
            save_maze_to_csv(self.maze, self.start, self.end)
        else:
            messagebox.showwarning("未找到迷宫", "请先创建或加载一个迷宫")

    def load_maze(self):
        self.maze, self.start, self.end = load_maze_from_csv()
        if self.maze is not None:
            self.update_maze()

    def update_maze(self):
        self.canvas.delete("all")
        if self.maze is None:
            return
        for i in range(self.maze.shape[0]):
            for j in range(self.maze.shape[1]):
                color = 'black' if self.maze[i, j] == 1 else 'white'
                self.canvas.create_rectangle(
                    j * self.cell_size, i * self.cell_size,
                    (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                    fill=color, outline='gray'
                )
        if self.start:
            self.canvas.create_text(
                self.start[1] * self.cell_size + self.cell_size / 2,
                self.start[0] * self.cell_size + self.cell_size / 2,
                text='S', fill='green'
            )
        if self.end:
            self.canvas.create_text(
                self.end[1] * self.cell_size + self.cell_size / 2,
                self.end[0] * self.cell_size + self.cell_size / 2,
                text='E', fill='red'
            )

    def update_status(self, message):
        self.status_text.insert(tk.END, message + '\n')
        self.status_text.see(tk.END)

class NewMazeDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent  # 保存父级引用
        self.title('新建迷宫')
        self.geometry('300x200')
        self.maze = None
        self.start = None
        self.end = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="宽度:").pack()
        self.width_entry = tk.Entry(self)
        self.width_entry.pack()

        tk.Label(self, text="高度:").pack()
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        tk.Label(self, text="复杂度:").pack()
        self.complexity_entry = tk.Entry(self)
        self.complexity_entry.pack()

        tk.Button(self, text="新建空白迷宫", command=self.create_blank_maze).pack(pady=5)
        tk.Button(self, text="新建随机迷宫", command=self.create_random_maze).pack(pady=5)

        # 确保对话框获取焦点
        self.grab_set()
        self.focus_set()

    def create_blank_maze(self):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            self.maze = np.zeros((height, width), dtype=int)
            self.start = (0, 0)
            self.end = (height - 1, width - 1)
            self.destroy()
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的宽度和高度")

    def create_random_maze(self):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            complexity = int(self.complexity_entry.get())
            self.maze = self.parent.solver.generate_maze_dfs(width, height)
            self.start = (0, 0)
            self.end = (height - 1, width - 1)
            self.destroy()
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的宽度、高度和复杂度")
