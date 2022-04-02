"""This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?"""

from collections import defaultdict, namedtuple

from dcp import harness


def solution(nums):
    """optimal subproblem: solution(n) is max(solution(n-1), solution(n-2) + num_n)

    runtime: O(n)
    space: O(n)
    """
    if not nums:
        return 0

    counts = defaultdict(int)
    for i, num in enumerate(nums):
        counts[i] = max(counts[i - 1], counts[i - 2] + num)

    return counts[len(nums) - 1]


def solution_space_light(nums):
    """Make it space lighter by only including the last two solutions"""
    counts = [0, 0]
    for num in nums:
        n_2 = counts.pop(0)
        counts.append(max(counts[-1], n_2 + num))

    return counts[1]


if __name__ == "__main__":
    tc = namedtuple("TestCase", "nums expected")
    cases = (
        tc([], 0),
        tc([3], 3),
        tc([3, 4], 4),
        tc([3, 4, 2], 5),
        tc([2, 4, 6, 2, 5], 13),
        tc([5, 1, 1, 5], 10),
    )

    harness(cases, lambda t: solution_space_light(t.nums))
