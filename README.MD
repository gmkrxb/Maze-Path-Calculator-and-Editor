# Maze Path Calculator and Editor

<div align="center">
  <a href="#english">English</a> | <a href="#中文">中文</a>
</div>

## English

### Introduction
The Maze Path Calculator and Editor is a comprehensive tool designed for creating, editing, and solving mazes. It allows users to generate random mazes, set start and end points, and find the shortest or all possible paths within the maze. Additionally, users can interactively edit the maze and execute custom scripts to manipulate the maze layout.

### Features
- **Maze Generation:** Create blank or random mazes of specified dimensions and complexity.
- **Maze Editing:** Use pencil and eraser tools to draw and erase walls. Set start and end points.
- **Path Finding:** Calculate the shortest path and count all possible paths from start to end.
- **Maze Validation:** Check if the maze is solvable from start to end.
- **Code Execution:** Write and execute custom scripts to manipulate the maze layout in real-time.
- **Save/Load Mazes:** Save and load mazes as CSV files.

### Installation
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Run the main application:
    ```bash
    python main.py
    ```
2. Use the main interface to load mazes, find paths, or open the maze editor.
3. In the maze editor, use the top panel to create, save, load mazes, or switch tools (pencil, eraser).
4. Use the bottom status bar to see the results of path calculations or code execution.
5. Write and execute custom scripts in the code editor to manipulate the maze.

### Dependencies
- pandas
- numpy
- tkinter

### File Structure
- `main.py`: Entry point of the application.
- `maze_gui.py`: Main application GUI.
- `maze_editor.py`: Maze editor GUI.
- `maze_code_executor.py`: Code executor for custom scripts.
- `maze_utilities.py`: Utility functions for maze operations.
- `maze_solver.py`: Core logic for path finding and maze generation.
- `shortest_path_solver.py`: Algorithm for finding the shortest path.
- `all_paths_solver.py`: Algorithm for counting all paths.

## 中文

### 简介
迷宫路径计算器和编辑器是一个全面的工具，用于创建、编辑和解决迷宫。它允许用户生成随机迷宫、设置起点和终点，并找到迷宫内的最短路径或所有可能路径。此外，用户可以交互式编辑迷宫并执行自定义脚本来操作迷宫布局。

### 特性
- **迷宫生成：** 创建指定尺寸和复杂度的空白或随机迷宫。
- **迷宫编辑：** 使用画笔和橡皮工具绘制和擦除墙壁。设置起点和终点。
- **路径寻找：** 计算从起点到终点的最短路径和所有可能路径。
- **迷宫验证：** 检查迷宫从起点到终点是否可通行。
- **代码执行：** 编写和执行自定义脚本以实时操作迷宫布局。
- **保存/加载迷宫：** 保存和加载迷宫为CSV文件。

### 安装
1. 克隆仓库：
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. 安装所需包：
    ```bash
    pip install -r requirements.txt
    ```

### 使用
1. 运行主应用程序：
    ```bash
    python main.py
    ```
2. 使用主界面加载迷宫、寻找路径或打开迷宫编辑器。
3. 在迷宫编辑器中，使用顶部面板创建、保存、加载迷宫或切换工具（画笔、橡皮）。
4. 使用底部状态栏查看路径计算或代码执行的结果。
5. 在代码编辑器中编写并执行自定义脚本以操作迷宫。

### 依赖
- pandas
- numpy
- tkinter

### 文件结构
- `main.py`：应用程序的入口点。
- `maze_gui.py`：主应用程序GUI。
- `maze_editor.py`：迷宫编辑器GUI。
- `maze_code_executor.py`：用于自定义脚本的代码执行器。
- `maze_utilities.py`：迷宫操作的实用函数。
- `maze_solver.py`：路径寻找和迷宫生成的核心逻辑。
- `shortest_path_solver.py`：用于寻找最短路径的算法。
- `all_paths_solver.py`：用于计算所有路径的算法。
