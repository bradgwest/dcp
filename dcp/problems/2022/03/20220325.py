"""Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from collections import namedtuple

from dcp import harness


def solution(l, k):
    d = set()
    for a in l:
        b = k - a
        if b in d:
            return True
        d.add(a)
    return False


if __name__ == "__main__":
    tc = namedtuple("TestCase", "l k expected")

    cases = (tc([10, 15, 3, 7], 17, True), tc([3, 4, 5], 10, False))
    harness(cases, lambda t: solution(t.l, t.k))
