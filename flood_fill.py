from collections import deque
from maze import Maze, DIRS

def flood_fill(maze, goal):
    distances_dict = {goal: 0} #Track visited cells
    q = deque([goal]) #Append the starting point
    while len(q) > 0:
        visited_x, visited_y = q.popleft()
        for coord in maze.neighbors(visited_x, visited_y):
            if coord not in distances_dict:
                distances_dict[(coord)] = distances_dict[(visited_x, visited_y)] + 1
                q.append(coord)
    return distances_dict

def next_step(distances, maze, pos):
    x, y = pos
    cell_paths = maze.neighbors(x, y)

    best_path = None
    for cell in cell_paths:
        if cell in distances:
            if best_path is None or distances[cell] < distances[best_path]:
                best_path = cell
    if best_path is None:
        raise ValueError("Mouse trapped! Nowhere to go")
    return best_path

def print_distances(distances, size):
    for y in range(size):
        row = ""
        for x in range(size):
            if (x, y) in distances:
                row += f"{distances[(x, y)]:3}"
            else:
                row += f"{'.':>3}"
        print(row)

def run_mouse(real_maze, start, goal):
    known_walls = Maze(real_maze.size)
    pos = start
    path = [pos]
    refloods = 0
    distances = flood_fill(known_walls, goal)

    steps = 0
    while pos != goal:
        x, y = pos
        new_wall_found = False

        for side in DIRS:
            if real_maze.has_wall(x, y, side) and not known_walls.has_wall(x, y, side):
                known_walls.add_wall(x, y, side)
                new_wall_found = True

        if new_wall_found:
            distances = flood_fill(known_walls, goal)
            refloods += 1 

        pos = next_step(distances, known_walls, pos)
        path.append(pos)
        steps += 1
    return path, refloods

# Paste this at the bottom of flood_fill.py (after run_mouse)

def mouse_steps(real_maze, start, goal):
    """Same logic as run_mouse, but yields a snapshot at every cell so a GUI can animate it."""
    known_walls = Maze(real_maze.size)
    pos = start
    path = [pos]
    refloods = 0
    distances = flood_fill(known_walls, goal)
    steps = 0
    while True:
        x, y = pos
        new_wall_found = False
        if pos != goal:                      # like run_mouse, stop sensing once at the goal
            for side in DIRS:
                if real_maze.has_wall(x, y, side) and not known_walls.has_wall(x, y, side):
                    known_walls.add_wall(x, y, side)
                    new_wall_found = True
            if new_wall_found:
                distances = flood_fill(known_walls, goal)
                refloods += 1
        yield {
            "pos": pos,
            "known": known_walls,
            "distances": distances,
            "path": list(path),
            "refloods": refloods,
            "new_wall": new_wall_found,
            "done": pos == goal,
        }
        if pos == goal:
            return
        pos = next_step(distances, known_walls, pos)
        path.append(pos)
        steps += 1
        if steps > 1000:
            raise RuntimeError("mouse never reached the goal")