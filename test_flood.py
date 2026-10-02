from maze import Maze
from flood_fill import flood_fill, next_step, run_mouse


def test_open_maze_distances():
    m = Maze(4)
    d = flood_fill(m, (3, 3))
    assert d[(0, 0)] == 6
    assert len(d) == 16


def test_walls_are_mirrored():
    m = Maze(4)
    m.add_wall(1, 1, "E")
    assert m.has_wall(1, 1, "E")
    assert m.has_wall(2, 1, "W")


def test_wall_forces_detour():
    m = Maze(4)
    m.add_wall(3, 2, "S")            # blocks (3, 2) from (3, 3)
    d = flood_fill(m, (3, 3))
    assert d[(3, 2)] == 3            # it was 1 with no wall
    assert d[(0, 0)] == 6


def test_next_step_moves_toward_goal():
    m = Maze(4)
    d = flood_fill(m, (3, 3))
    assert next_step(d, m, (3, 2)) == (3, 3)


def test_mouse_reaches_goal_and_refloods():
    true_maze = Maze(4)
    true_maze.add_wall(0, 0, "E")
    true_maze.add_wall(1, 1, "S")
    path, refloods = run_mouse(true_maze, (0, 0), (3, 3))
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)
    assert refloods >= 1


def test_mouse_never_crosses_a_wall():
    true_maze = Maze(4)
    true_maze.add_wall(0, 0, "E")
    true_maze.add_wall(1, 1, "S")
    path, refloods = run_mouse(true_maze, (0, 0), (3, 3))
    for i in range(len(path) - 1):
        x, y = path[i]
        assert path[i + 1] in true_maze.neighbors(x, y)


if __name__ == "__main__":
    test_open_maze_distances()
    test_walls_are_mirrored()
    test_wall_forces_detour()
    test_next_step_moves_toward_goal()
    test_mouse_reaches_goal_and_refloods()
    test_mouse_never_crosses_a_wall()
    print("All tests passed")