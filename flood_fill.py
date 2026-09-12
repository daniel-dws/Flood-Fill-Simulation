from collections import deque

def flood_fill(maze, start):
    distances_dict = {start: 0} #Track visited cells
    q = deque([start]) #Append the starting point
    while len(q) > 0:
        visited_x, visited_y = q.popleft()
        for coord in maze.neighbors(visited_x, visited_y):
            if coord not in distances_dict:
                distances_dict[(coord)] = distances_dict[(visited_x, visited_y)] + 1
                q.append(coord)
    return distances_dict

#Old dead code
"""
from collections import deque

def flood_fill(maze, start):
    distances_dict = {start: 0} #Track visited cells
    q = deque([start]) #Append the starting point
    while len(q) > 0:
        visited_x, visited_y = q.popleft()
        if (visited_x, visited_y) in distances_dict:
            visit
            for coord in maze.neighbors(visited_x, visited_y):
                if coord not in distances_dict:
                    q.append(coord)
        else:
            distances_dict[(visited_x, visited_y)] = 

hint which part of this algo is wrong
```
"""