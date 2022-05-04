"""This problem was asked by Facebook.

You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two walls
get filled up.

Compute how many units of water remain trapped on the map in O(N) time and
O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would
run off to the left), so we can trap 8 units of water.
"""


def capacity(elevation):
    total = 0
    max_i = elevation.index(max(elevation))

    left_max = elevation[0]
    for num in elevation[1:max_i]:
        if num < left_max:
            total += left_max - num
        left_max = max(left_max, num)

    right_max = elevation[-1]
    for num in elevation[-2:max_i:-1]:
        if num < right_max:
            total += right_max - num
        right_max = max(right_max, num)

    return total


print(capacity([3, 4, 3, 5]))
print(capacity([2, 1, 2]))
print(capacity([3, 0, 1, 3, 0, 5]))
print(capacity([5, 3, 1, 3, 0]))
