import tkinter as tk
import time

def solve_maze(maze, start, end):
    # Create a stack for DFS
    stack = []
    # Push the starting point to the stack
    stack.append(start)

    # Mark the starting point as visited
    maze[start[0]][start[1]] = 2

    # Define a 4-directional array to move in the maze
    # up, right, down, left
    row = [-1, 0, 1, 0]
    col = [0, 1, 0, -1]

    # Keep visiting the next unvisited cell until the stack is empty
    while stack:
        # Pop the last cell from the stack
        current = stack.pop()
        i, j = current[0], current[1]

        # Check if the current cell is the end
        if current == end:
            return True

        # Visit all the unvisited neighbors
        for k in range(4):
            x, y = i + row[k], j + col[k]
            if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 0:
                stack.append((x, y))
                maze[x][y] = 2
                draw_path(x, y)
                time.sleep(0.5)

    return False

def draw_path(x, y):
    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill="green")
    window.update()

def draw_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill="black")

# Example maze
maze = [[0, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]
start = (0, 0)
end = (len(maze) - 1, len(maze[0]) - 1)

# Set up the window
window = tk.Tk()
window.title("Gangester Amol")
cell_size = 50
canvas = tk.Canvas(window, width=len(maze[0]) * cell_size, height=len(maze) * cell_size)
canvas.pack()

# Draw the maze
draw_maze(maze)

# Call the solve_maze function
if solve_maze(maze, start, end):
    print("The maze has a solution!")
else:
    print("The maze has no solution.")

# Show the window
window.mainloop()
