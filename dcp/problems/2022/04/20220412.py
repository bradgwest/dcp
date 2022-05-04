"""This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different
colors. He has a goal of minimizing cost while ensuring that no two
neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to
build the nth house with kth color, return the minimum cost which achieves
this goal.

         colors
          r g b
houses  1 4 5 3
        2 3 4 1
        3 4 2 1
        4 1 3 2
        5 1 3 1

  r g b
1 8 9 9
2 1 8 8
3 2 2 2
"""

from collections import namedtuple
from math import inf


def solution(matrix):
    """ """
    k = len(matrix[0])
    soln_row = [0] * k

    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(soln_row[i] for i in range(k) if i != c) + val)
        soln_row = row_cost
    return min(soln_row)


tc = namedtuple("TestCase", "m expected")

cases = (
    tc(
        [[4, 5, 3], [2, 4, 1], [4, 2, 1]],
        6,
    ),
    tc([[8, 9, 9], [1, 8, 8], [2, 2, 2]], 12),
)
print(solution(cases[0].m))
print(solution(cases[1].m))
# harness(cases, lambda t: solution(t.m))
