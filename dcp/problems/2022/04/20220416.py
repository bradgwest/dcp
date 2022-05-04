"""This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the
minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down,
and right. You cannot move through walls. You cannot wrap around the edges of
the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
number of steps required to reach the end is 7, since we would need to go
through (1, 2) because there is a wall everywhere else on the second row.
"""


def fill(matrix, x, y, distance):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix):
        return

    cell_val = matrix[x][y]
    # wall or already set by shorter path
    if cell_val is True:
        return

    new_val = distance
    if cell_val is not False and new_val >= cell_val:
        return

    matrix[x][y] = new_val
    for new_x, new_y in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
        fill(matrix, new_x, new_y, new_val + 1)


def path(matrix, start, end):
    """
    Radiate out from the start coordinate, building out the distance from that
    point. Then return the value at the end point.

    runtime: O(mn)
    space: O(mn)
    """
    fill(matrix, start[0], start[1], 0)
    return matrix[end[0]][end[1]]


m = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False],
]
print(path(m, (3, 0), (0, 0)))

m = [
    [True, False, False, False],
    [True, True, True, False],
    [False, False, True, False],
    [False, False, False, False],
]
print(path(m, (2, 1), (0, 1)))
