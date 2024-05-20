import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def load_maze_from_csv():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not filepath:
        return None, None, None
    try:
        df = pd.read_csv(filepath, header=None)
        df_values = df.replace({'S': 0, 'E': 0}).values
        start = tuple(df[df == 'S'].stack().index.tolist()[0])
        end = tuple(df[df == 'E'].stack().index.tolist()[0])
        return df_values, start, end
    except FileNotFoundError:
        messagebox.showerror("错误", "找不到迷宫文件")
        return None, None, None
    except Exception as e:
        messagebox.showerror("错误", f"加载迷宫时出错: {e}")
        return None, None, None

def save_maze_to_csv(maze, start, end):
    filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not filepath:
        return
    df = pd.DataFrame(maze, dtype=str)  # 将数据框转换为字符串类型
    df.iloc[start[0], start[1]] = 'S'
    df.iloc[end[0], end[1]] = 'E'
    df.to_csv(filepath, index=False, header=False)
    messagebox.showinfo("保存成功", f"迷宫已成功保存到 {filepath}")

def display_maze(canvas, maze, start, end, path=None):
    canvas.delete("all")
    if maze is None:
        return
    height, width = len(maze), len(maze[0])
    cell_width = min(canvas.winfo_width() / width, canvas.winfo_height() / height)
    cell_height = cell_width

    x_offset = (canvas.winfo_width() - width * cell_width) / 2
    y_offset = (canvas.winfo_height() - height * cell_height) / 2

    for i in range(height):
        for j in range(width):
            color = 'black' if maze[i][j] == 1 else 'white'
            canvas.create_rectangle(
                x_offset + j * cell_width, y_offset + i * cell_height,
                x_offset + (j + 1) * cell_width, y_offset + (i + 1) * cell_height,
                fill=color, outline='gray'
            )
            if (i, j) == start:
                canvas.create_text(
                    x_offset + j * cell_width + cell_width / 2,
                    y_offset + i * cell_height + cell_height / 2,
                    text='S', font=('Helvetica', 14), fill='green'
                )
            elif (i, j) == end:
                canvas.create_text(
                    x_offset + j * cell_width + cell_width / 2,
                    y_offset + i * cell_height + cell_height / 2,
                    text='E', font=('Helvetica', 14), fill='red'
                )
    if path:
        for (x, y) in path:
            canvas.create_rectangle(
                x_offset + y * cell_width, y_offset + x * cell_height,
                x_offset + (y + 1) * cell_width, y_offset + (x + 1) * cell_height,
                fill='red', outline='gray'
            )
