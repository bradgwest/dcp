"""There exists a staircase with N steps, and you can climb up either 1 or 2
steps at a time. Given N, write a function that returns the number of
unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could
climb any number from a set of positive integers X? For example, if X =
{1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

from collections import namedtuple

from dcp import harness


def ways(n):
    """
    runtime:
    space: O(n)
    """
    if n <= 0:
        return 0

    counts = [0] * n
    counts[0] = 1

    for i in range(1, n):
        if i == 1:
            counts[i] = 2
            continue
        counts[i] = counts[i - 2] + counts[i - 1]

    return counts[-1]


def general_ways(n, x):
    if n <= 0:
        return 0

    counts = [0] * (n + 1)
    counts[0] = 1

    for i in range(1, n + 1):
        for jump in x:
            if i - jump < 0:
                continue
            counts[i] += counts[i - jump]

    return counts[n]


if __name__ == "__main__":
    """
    1 1 1 1
    1 1 2
    2 1 1
    1 2 1
    3 1
    1 3
    2 2

    """
    tc = namedtuple("TestCase", "n jumps expected")
    cases = (
        tc(4, [1, 2], 5),
        tc(4, [1, 2, 3], 7),
    )

    harness(cases, lambda t: general_ways(t.n, t.jumps))
