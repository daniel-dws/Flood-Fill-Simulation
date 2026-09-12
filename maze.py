#Constant definitions
class Maze:
    def __init__(self, maze_obj):
        self.maze_obj = maze_obj
        self.ROW = len(maze_obj)
        self.COL = len(maze_obj[0])
    # def add_wall(self):
    #     pass
    # def has_wall(self):
    #     pass
    def neighbors(self, cur_x, cur_y):
        # try:
        accesible_directions = []
        up = cur_x - 1
        down = cur_x + 1
        left = cur_y - 1
        right = cur_y + 1

        if self.maze_obj[cur_x][cur_y] != 1:
            if up >= 0 and self.maze_obj[up][cur_y] == 0:
                accesible_directions.append((up, cur_y))
            if down < self.ROW and self.maze_obj[down][cur_y] == 0:
                accesible_directions.append((down, cur_y))
            if left >= 0 and self.maze_obj[cur_x][left] == 0:
                accesible_directions.append((cur_x, left))
            if right < self.COL and self.maze_obj[cur_x][right] == 0:
                accesible_directions.append((cur_x, right))
            return accesible_directions
        # except IndexError:
        #     print("Index out of bounds")

#Old dead code
# maze_obj = [
#     [0, 0, 1, 1],
#     [1, 0, 1, 1],
#     [1, 0, 0, 1],
#     [1, 1, 0, 1]
# ]

# maze = Maze(maze_obj)
# print(maze.neighbor(2, 1))