"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
"""
from collections import namedtuple

from dcp import harness


def brute(nums):
    positive = [i for i in sorted(nums) if i > 0]
    if not positive:
        return 1

    for i, v in enumerate(positive):
        if i + 1 != v:
            return i + 1
    return len(positive) + 1


def solution(nums):
    if not nums:
        return 1

    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break

    print(f"ordered: {nums}")
    for i, num in enumerate(nums, 1):
        if num != i:
            return i

    return len(nums) + 1


if __name__ == "__main__":
    tc = namedtuple("TestCase", "nums expected")

    cases = (
        tc([3, 4, -1, 1], 2),
        # tc([2, 3, -1, 1], 4),
        # tc([1, 2, 0], 3),
        # tc([-1], 1),
        # tc([], 1),
        # tc([0], 1),
        # tc([0, 1], 2),
        # tc([1, 1, 1], 2),
    )
    harness(cases, lambda t: solution(t.nums))
