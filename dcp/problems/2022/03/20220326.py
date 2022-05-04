"""Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
"""

import math
from collections import namedtuple

from dcp import harness


def solution(l):
    """
    runtime: O(n)
    memory: O(n)
    """
    p = math.prod(l)
    return [p // x for x in l]


def solution_wo_div_brute_force(l):
    """
    runtime: O(n^2)
    memory: O(n)
    """
    output = [1] * len(l)
    for i, v in enumerate(l):
        for j, o in enumerate(output):
            if i == j:
                continue
            output[j] = o * v
    return output


def solution_wo_div(nums):
    """
    runtime: O(n)
    memory: O(n)
    """
    prefix_products = [nums[0]]
    for num in nums[1:]:
        prefix_products.append(prefix_products[-1] * num)
    print(f"prefix: {prefix_products}")

    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    # reverse it so that the indexing works based on i
    suffix_products = list(reversed(suffix_products))
    print(f"suffix: {suffix_products}")

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


if __name__ == "__main__":
    tc = namedtuple("TestCase", "input expected")

    cases = (tc([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]), tc([3, 2, 1], [2, 3, 6]))
    # harness(cases, lambda t: solution(t.input))
    harness(cases, lambda t: solution_wo_div(t.input))
