# Flood Fill Simulation

A Micromouse maze solver in Python. The mouse discovers walls as it moves and re-floods the distance map from the goal.

## Demo

Visualization of the mouse solving a maze (distance numbers update as new walls are found):

https://github.com/user-attachments/assets/a57566f8-5132-45bb-b497-3ba224b2f9ee

## How it works

- Walls are stored between cells, and each wall is mirrored on the neighboring cell.
- A BFS from the goal gives every cell its distance to the goal.
- The mouse knows where the goal is, but it only senses the walls of the cell it is standing in.
- When it discovers a new wall, it re-floods the distances from the goal and steps to the lowest-numbered neighbor.

## Files

- `maze.py`: maze and wall storage
- `flood_fill.py`: BFS flood fill, `next_step`, and `run_mouse`
- `test_flood.py`: tests

## Run

Requires Python 3 and no extra libraries.

```
python flood_fill.py
python test_flood.py
```

## Tests

The tests check that walls are mirrored, that a wall forces a detour, that the mouse moves toward the goal, that it never crosses a wall, and that it reaches the goal and re-floods when it finds new walls.
