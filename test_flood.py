from maze import Maze
from flood_fill import flood_fill

maze_obj = [
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1]
]
maze = Maze(maze_obj)
print(flood_fill(maze, (0, 0)))
