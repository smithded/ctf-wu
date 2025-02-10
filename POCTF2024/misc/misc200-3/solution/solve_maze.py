#!/usr/bin/python3

from PIL import Image, ImageDraw

# Load the maze image
maze_path = "Misc200-3.png"
maze_img = Image.open(maze_path)

# Maze solving libraries
import cv2
import numpy as np

# Convert the image to binary (black and white)
maze_cv = cv2.imread(maze_path, cv2.IMREAD_GRAYSCALE)
_, binary_maze = cv2.threshold(maze_cv, 128, 255, cv2.THRESH_BINARY_INV)

# Find the maze dimensions and define the start/end points (green/red)
height, width = binary_maze.shape
start = (1, 1)  # Green pixel is near top-left (1,1)
end = (width - 2, height - 2)  # Red pixel is near bottom-right

# Breadth-First Search (BFS) algorithm to solve the maze
def bfs(maze, start, end):
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {}
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_cell = (x + dx, y + dy)
            if (
                0 <= next_cell[0] < maze.shape[1]
                and 0 <= next_cell[1] < maze.shape[0]
                and maze[next_cell[1], next_cell[0]] == 255
                and next_cell not in visited
            ):
                visited.add(next_cell)
                parent[next_cell] = current
                queue.append(next_cell)
    # Backtrack to find the path
    path = []
    step = end
    while step != start:
        path.append(step)
        step = parent[step]
    path.append(start)
    return path[::-1]

# Solve the maze
path = bfs(binary_maze, start, end)

# Draw the solution path on the image with a thicker line
solved_maze = maze_img.convert("RGB")
draw = ImageDraw.Draw(solved_maze)
line_width = 5  # Increase line thickness for better visibility
better_color = (0, 0, 255)  # Blue color for better contrast

# Draw lines between consecutive path points
for i in range(1, len(path)):
    draw.line([path[i - 1], path[i]], fill=better_color, width=line_width)

# Save and display the solved maze
solved_maze_path = "solved_maze_thick_path.png"
solved_maze.save(solved_maze_path)
solved_maze.show()

print(f"Solved maze saved at: {solved_maze_path}")

