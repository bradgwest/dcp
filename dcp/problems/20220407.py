"""This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using
a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random


def estimate():
    """
    Gist:

    Draw a square, inscribe a circle in it. The area of the circle is
    (pi) * r^2. The area of the square is 4r^2. The difference in the areas can
    be estimated as the number of points that are inside the circle to the
    number of the points in the square:

    (pi * r^2) / (4 * r^2) = pi / 4 => 4 * A(circle) / A(square) = pi
    """
    r = 1
    # number of simulated points
    n = 100_000
    coords = [(random.uniform(0, r), random.uniform(0, r)) for _ in range(n)]
    in_circle = sum(x**2 + y**2 <= r**2 for x, y in coords)
    return 4 * in_circle / n


if __name__ == "__main__":
    for _ in range(10):
        print(estimate())
